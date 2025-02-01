from django.urls import path, include
from subscriptions.api.views.views_api_protected import ProtectedAPI
from subscriptions.api.views.views_purchase_subscription import PurchaseSubscriptionAPIView
from subscriptions.api.views.views_purchase_token import PurchaseTokensAPIView
from rest_framework.routers import DefaultRouter
from subscriptions.views import APIKeyUsageViewSet, APIKeyViewSet

router = DefaultRouter()
router.register(r'api_keys', APIKeyViewSet)
router.register(r'api_usage', APIKeyUsageViewSet, basename='api_usage')

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/protected/", ProtectedAPI.as_view(), name="protected-api"),

    path('purchase-subscription/', PurchaseSubscriptionAPIView.as_view(), name='purchase_subscription'),
    path('purchase-tokens/', PurchaseTokensAPIView.as_view(), name='purchase_tokens'),
]