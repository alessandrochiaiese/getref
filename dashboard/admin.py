from django.contrib import admin
from dashboard.models import * 

admin.site.register(Country) 
admin.site.register(Region) 
admin.site.register(Profile) 
admin.site.register(Business) 
admin.site.register(ProfileBusiness) 

