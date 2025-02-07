from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test, name='subscriptions-test'),
    path('plans/', views.plans, name='plans'),
    path('products/purchased/', views.purchased_products, name='purchased_products'),
    path('success/', views.success),
    path('cancel/', views.cancel),
]
