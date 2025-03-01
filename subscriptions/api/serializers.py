
from rest_framework import serializers
from subscriptions.models import APIKey 


class APIKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = APIKey
        fields = ['id', 'name', 'client_id', 'client_secret', 'created_at', 'last_used_at', 'request_count']