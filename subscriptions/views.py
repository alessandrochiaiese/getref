from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from oauth2_provider.models import Application
from django.conf import settings
from django.db import models
import uuid
from getref.settings import STRIPE_SECRET_KEY, STRIPE_ENDPOINT_SECRET

from subscriptions.utils import send_subscription_email
from subscriptions.models import *
from subscriptions.api.serializers import APIKeySerializer

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_stripe_subscription(user, plan):
    customer = stripe.Customer.create(email=user.email)
    subscription = stripe.Subscription.create(
        customer=customer.id,
        items=[{"price": "price_xxx"}]  # Price ID da Stripe Dashboard
    )
    return subscription.id

@login_required
def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            api_key = APIKey.objects.create(
                user=request.user, 
                client_type=Application.CLIENT_CONFIDENTIAL, 
                authorization_grant_type=Application.GRANT_CLIENT_CREDENTIALS,
                name=name
            )
            return redirect("home")
    api_keys = APIKey.objects.filter(user=request.user)
    return render(request, "subscriptions/home.html", {"api_keys": api_keys})


class APIKeyViewSet(viewsets.ModelViewSet):
    queryset = APIKey.objects.all()
    serializer_class = APIKeySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    @action(detail=True, methods=["POST"])
    def revoke(self, request, pk=None):
        api_key = self.get_object()
        api_key.delete()
        return Response({"message": "API Key revocata con successo!"}, status=200)
    
class APIKeyUsageViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        logs = APIUsageLog.objects.all()
        data = [{"api_key": log.api_key.name, "endpoint": log.endpoint, "timestamp": log.timestamp} for log in logs]
        return Response(data)
    from django.views.decorators.csrf import csrf_exempt


@login_required
def api_usage_dashboard(request):
    logs = APIUsageLog.objects.filter(api_key__user=request.user).order_by("-timestamp")[:20]
    return render(request, "subscriptions/api_usage_dashboard.html", {"logs": logs})


@csrf_exempt
def stripe_webhook_1(request):
    payload = request.body
    sig_header = request.headers.get("Stripe-Signature")
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET  #  "whsec_XXXX"

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except stripe.error.SignatureVerificationError as e:
        return JsonResponse({"error": "Webhook signature verification failed"}, status=400)

    if event["type"] == "customer.subscription.updated":
        subscription = event["data"]["object"]
        user = User.objects.get(email=subscription["customer_email"])
        api_key = APIKey.objects.get(user=user)
        api_key.plan = "pro" if "pro_plan" in subscription["items"]["data"][0]["plan"]["id"] else "free"
        api_key.save()

    return JsonResponse({"message": "Webhook ricevuto!"})

@csrf_exempt
def stripe_webhook_simple(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET  # Ottieni questa chiave da Stripe

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )

        # Gestisci il pagamento completato
        """if event['type'] == 'checkout.session.completed':
            session = event['data']['object']
            user_id = session['client_reference_id']
            plan_id = session['metadata']['plan_id']
            user = User.objects.get(id=user_id)
            plan = Plan.objects.get(id=plan_id)

            # Crea o aggiorna l'abbonamento
            subscription, created = Subscription.objects.get_or_create(user=user)
            subscription.plan = plan
            subscription.renew()

            return JsonResponse({'status': 'success'})"""
        
        if event['type'] == 'invoice.payment_succeeded':
            invoice = event['data']['object']
            user_id = invoice['customer']
            user = User.objects.get(stripe_customer_id=user_id)  # Usa l'ID cliente di Stripe
            plan_id = invoice['metadata']['plan_id']
            plan = Plan.objects.get(id=plan_id)

            # Trova o crea l'abbonamento
            subscription, created = Subscription.objects.get_or_create(user=user)
            subscription.plan = plan
            subscription.renew()

            # Invia un'email di rinnovo
            send_subscription_email(user, plan)
            return JsonResponse({'status': 'success'})
        
    except ValueError as e:
        # Event data is invalid
        return JsonResponse({'error': 'Invalid payload'}, status=400)
    except stripe.error.SignatureVerificationError as e:
        # Signature verification failed
        return JsonResponse({'error': 'Invalid signature'}, status=400)

    return JsonResponse({'status': 'success'})

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    endpoint_secret = STRIPE_ENDPOINT_SECRET  # Ottieni questa chiave da Stripe

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )

        # Se l'evento riguarda un pagamento completato
        if event['type'] == 'checkout.session.completed':
            session = event['data']['object']
            user_id = session['client_reference_id']
            package_id = session['metadata']['package_id']
            user = User.objects.get(id=user_id)
            package = TokenPackage.objects.get(id=package_id)

            # Trova o crea il record dei token per l'utente
            token_record, created = Token.objects.get_or_create(user=user)
            token_record.add_tokens(package.tokens)

            return JsonResponse({'status': 'success'})

    except ValueError as e:
        return JsonResponse({'error': 'Invalid payload'}, status=400)
    except stripe.error.SignatureVerificationError as e:
        return JsonResponse({'error': 'Invalid signature'}, status=400)

    return JsonResponse({'status': 'success'})
