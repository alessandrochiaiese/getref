# accounts/urls.py
from django.urls import include, path
from accounts.views.views_account import SignUpView


urlpatterns = [
    # APIs
    path('', include('accounts.api.urls')),
 
    # Signup
    #path("signup/", SignUpView.as_view(), name="signup"),
]