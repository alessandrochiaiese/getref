from django.urls import path
from django.urls import include
from oauth2_provider import urls as oauth2_urls
from accounts.api.views.views_group import GroupList
from accounts.api.views.views_user import UserList, UserDetails 

urlpatterns = [
    # oauth 
    path("accounts/", include("django.contrib.auth.urls")),   
    
    # rest framework
    path('o/', include(oauth2_urls)),
    path('users/', UserList.as_view(), name='custom_users'),
    path('users/<pk>/', UserDetails.as_view(), name='custom_user'),
    path('groups/', GroupList.as_view(), name='custom_groups'),
]
