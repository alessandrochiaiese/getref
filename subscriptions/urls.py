from django.urls import path
from . import views

urlpatterns = [
    #path('subscriptions/', views.home, name='subscriptions-home'),
    path('plans/', views.plans, name='plans'),
    path('success/', views.success),
    path('cancel/', views.cancel),
]
