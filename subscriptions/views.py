from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.views import APIView
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from getref.settings import STRIPE_SECRET_KEY, STRIPE_ENDPOINT_SECRET
from rest_framework.decorators import action

from subscriptions.utils import send_subscription_email
from subscriptions.models import *
from subscriptions.api.serializers import APIKeySerializer

from django.contrib.auth.decorators import login_required
import stripe

from django.http import JsonResponse
from django.conf import settings


from django.db import models
from oauth2_provider.models import Application
from django.utils.timezone import now
import uuid

#stripe.api_key = STRIPE_SECRET_KEY
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
    return render(request, "home.html", {"api_keys": api_keys})

class APIKey(Application):
    created_at = models.DateTimeField(auto_now_add=True)
    last_used_at = models.DateTimeField(null=True, blank=True)
    request_count = models.PositiveIntegerField(default=0)

    def update_usage(self):
        self.last_used_at = now()
        self.request_count += 1
        self.save()

class APIUsageLog(models.Model):
    api_key = models.ForeignKey(APIKey, on_delete=models.CASCADE)
    endpoint = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.api_key} -> {self.endpoint} at {self.timestamp}"
    
class MyLoggingView(APIView):
    def get(self, request):
        APIUsageLog.objects.create(
            api_key=request.headers.get("Authorization", "unknown"),
            endpoint=request.path
        )
        return Response({"message": "Logged successfully!"})
    
class PurchaseTokensAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        package_id = request.data.get('package_id')  # L'ID del pacchetto scelto dall'utente
        user = request.user
        package = get_object_or_404(TokenPackage, id=package_id)

        try:
            # Crea una sessione di pagamento Stripe
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'eur',
                        'product_data': {
                            'name': f'Acquisto {package.name} ({package.tokens} token)',
                        },
                        'unit_amount': package.price_in_cents,  # Prezzo del pacchetto in centesimi
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url='https://your-site.com/success/',  # URL di successo
                cancel_url='https://your-site.com/cancel/',  # URL di cancellazione
                client_reference_id=user.id,  # Passiamo l'ID dell'utente
                metadata={'package_id': package.id},
            )

            return Response({
                "session_id": checkout_session.id
            })

        except stripe.error.StripeError as e:
            return Response({"error": str(e)}, status=400)


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
@login_required
def api_usage_dashboard(request):
    logs = APIUsageLog.objects.filter(api_key__user=request.user).order_by("-timestamp")[:20]
    return render(request, "api_usage_dashboard.html", {"logs": logs})

class APIKeyUsageViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        logs = APIUsageLog.objects.all()
        data = [{"api_key": log.api_key.name, "endpoint": log.endpoint, "timestamp": log.timestamp} for log in logs]
        return Response(data)
    from django.views.decorators.csrf import csrf_exempt


stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.headers.get("Stripe-Signature")
    endpoint_secret = "whsec_XXXX"

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
