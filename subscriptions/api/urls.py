from django.urls import path, include
from subscriptions.api.views.views_api_protected import ProtectedAPI
from subscriptions.api.views.views_promotions import create_promotion
from subscriptions.api.views.views_purchase_subscription import PurchaseSubscriptionAPIView
from subscriptions.api.views.views_purchase_token import PurchaseTokensAPIView
#from rest_framework.routers import DefaultRouter

#router = DefaultRouter()
#router.register(r'api-keys', APIKeyViewSet)
#router.register(r'api-usage', APIKeyUsageViewSet, basename='api_usage')

urlpatterns = [
    #path('', include(router.urls)),
    #path('protected/', ProtectedAPI.as_view(), name="protected-api"),
    path('create-promotion/', create_promotion, name='create_promotion'),

    path('purchase-subscription/', PurchaseSubscriptionAPIView.as_view(), name='purchase-subscription'),
    path('purchase-tokens/', PurchaseTokensAPIView.as_view(), name='purchase-tokens'),
]