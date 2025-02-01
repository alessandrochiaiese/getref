from django.contrib import admin
from subscriptions.models.plan import Plan 

admin.site.register(Plan) 

from subscriptions.models import APIKey, APIUsageLog

@admin.register(APIKey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = ("name", "client_id", "last_used_at", "request_count")

@admin.register(APIUsageLog)
class APIUsageLogAdmin(admin.ModelAdmin):
    list_display = ("api_key", "endpoint", "timestamp")