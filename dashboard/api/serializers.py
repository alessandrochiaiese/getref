# dashboard/api/serializers.py

from rest_framework import serializers
from dashboard.models import Profile, Region

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'avatar', 'bio', 'birth_date', 'city', 'street', 'CAP', 'phone_number', 'is_business', 'is_buyer', 'company_name', 'is_owner', 'iva', 'contact_number' ]

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name', 'latitude', 'longitude' ]
