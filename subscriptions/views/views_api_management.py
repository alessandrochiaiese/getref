from django.http import HttpResponse, JsonResponse
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
from getref.settings import DOMAIN, STRIPE_SECRET_KEY, STRIPE_ENDPOINT_SECRET

from subscriptions.models.stripe_customer import StripeCustomer
from subscriptions.utils import send_subscription_email
from subscriptions.models import *
from subscriptions.api.serializers import APIKeySerializer

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def api_keys_dashboard(request):
    api_keys = APIKey.objects.filter(user=request.user)  # Puoi limitare le chiavi API a un utente
    return render(request, 'subscriptions/api_keys_dashboard.html', {'api_keys': api_keys})
"""
@login_required
def create_api_key(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            api_key = APIKey.objects.create(
                user=request.user, 
                client_type=Application.CLIENT_CONFIDENTIAL, 
                authorization_grant_type=Application.GRANT_CLIENT_CREDENTIALS,
                name=name
            )
            return redirect("subscription-home")
    api_keys = APIKey.objects.filter(user=request.user)
    return render(request, "subscriptions/home.html", {"api_keys": api_keys})
"""
@login_required
def create_api_key(request):
    if request.method == "POST":
        name = request.POST['name']
        plan = request.POST.get('plan', 'free')
        new_api_key = APIKey.objects.create(name=name, plan=plan, client_id="generated-client-id")
        return redirect('api_keys_dashboard')
    return render(request, 'create_api_keys.html')

@login_required
def api_usage_dashboard(request):
    logs = APIUsageLog.objects.filter(api_key__user=request.user).order_by("-timestamp")[:20]
    return render(request, "subscriptions/api_usage_dashboard.html", {"logs": logs})

@login_required
def subscribe(request):
    subscription = StripeSubscription.objects.get(user=request.user)
    plans = Plan.objects.all()
    return render(request, 'subscriptions/create_api_keys.html', {'subscription': subscription, 'plans': plans})

# API per eliminare la chiave
@login_required
def delete_api_key(request, key_id):
    try:
        key = APIKey.objects.get(id=key_id)
        key.delete()
        return JsonResponse({'status': 'success'})
    except APIKey.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'API key not found'}, status=404)
    
@login_required
def email_subscription_success(request) -> HttpResponse:
    return render(request, "subscriptions/email_subscription_success.html")
