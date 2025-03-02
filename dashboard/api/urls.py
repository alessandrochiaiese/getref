from django.urls import path 
from dashboard.api.views.views_profile import ProfileAPIView, UserProfileDataView
from dashboard.api.views.views_region import RegionAPIView
 
urlpatterns = [  
    path('profiles/', ProfileAPIView.as_view(), name='profiles'),
    path('profiles/<int:profile_id>/', ProfileAPIView.as_view(), name='profile'),
 
    path('regions/', RegionAPIView.as_view(), name='regions'),
    path('regions/<int:region_id>/', RegionAPIView.as_view(), name='region'),
 
    # Dati profilo utente
    path('profile/data/', UserProfileDataView.as_view(), name='core_profile_data'),
]
