
from django.conf.urls.static import static
from django.urls import include, path, re_path as url

from getref import settings 
from .views import stripe_webhook

urlpatterns = [
    path('stripe/webhook/', stripe_webhook, name='stripe-webhook'),
    
    path('api/v0/', include('subscriptions.api.urls'), name='subscriptions'),
] 