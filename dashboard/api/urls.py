from django.urls import path 
from dashboard.api.views.views_profile import ProfileAPIView, UserProfileDataView
 
urlpatterns = [  
    path('profiles/', ProfileAPIView.as_view(), name='profiles'),
    path('profiles/<int:profile_id>/', ProfileAPIView.as_view(), name='profile'),
 
    # Dati profilo utente
    path('profile/data/', UserProfileDataView.as_view(), name='core_profile_data'),
]
