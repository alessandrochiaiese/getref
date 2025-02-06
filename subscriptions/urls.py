from django.urls import path
from . import views

urlpatterns = [
    path('plans/', views.home, name='subscriptions-home'),
    path('success/', views.success),
    path('cancel/', views.cancel),
]
