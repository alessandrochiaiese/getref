from django.urls import path
from . import views

urlpatterns = [
    # tests
    path('test/', views.test, name='subscriptions-test'),
    # products
    path('products/', views.products, name='product_list'),
    path('products/purchased/', views.purchased_products, name='purchased_products'),
    # subscriptions
    path('plans/', views.plans, name='plans'),
    path('success/', views.success),
    path('cancel/', views.cancel),
]
