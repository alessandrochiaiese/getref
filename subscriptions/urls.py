
from django.conf.urls.static import static
from django.urls import include, path, re_path as url

from getref import settings 
from .views import create_stripe_subscription, stripe_webhook, home, api_keys, api_usage_dashboard, email_subscription_success

urlpatterns = [
    path('subscriptions/', home, name='subscription-home'),
    path('subscriptions/api-keys/', api_keys, name='subscription-api-keys'),
    path('subscriptions/api-usage-dashboard/', api_usage_dashboard, name='subscription-api-usage-dashboard'),
    path('subscriptions/email-subscription-success/', email_subscription_success, name='subscription-email-subscription-success'),
    path('subscriptions/create/<int:plan>/', create_stripe_subscription, name='subscription-create'),
    
    path('stripe/webhook/', stripe_webhook, name='stripe-webhook'),

    path('api/v0/', include('subscriptions.api.urls'), name='api-subscriptions'),
] 