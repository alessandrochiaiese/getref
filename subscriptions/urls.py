from django.urls import path
from .views import views_subscription
from .views import views_promotion

urlpatterns = [
    # tests
    path('test/', views_subscription.test, name='subscriptions-test'),

    # promotions
    path('my_promotions/', views_promotion.my_promotions, name='my_promotions'),
    #path('promote/', views_promotion.promote, name='stripe_promote'),
    path('promotion_sales/', views_promotion.promotion_sales, name='promotion_sales'),
    
    # products
    path('products/', views_subscription.products, name='product_list'),
    path('products/purchased/', views_subscription.purchased_products, name='purchased_products'),

    # subscriptions
    path('plans/', views_subscription.plans, name='plans'),
    path('success/', views_subscription.success),
    path('cancel/', views_subscription.cancel),
]
