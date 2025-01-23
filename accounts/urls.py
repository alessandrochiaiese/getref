# accounts/urls.py
from django.urls import include, path

urlpatterns = [
    # APIs
    path('', include('accounts.api.urls')),

]