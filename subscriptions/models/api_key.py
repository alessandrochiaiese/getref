from oauth2_provider.models import Application
from django.db import models

class APIKey(Application):
    #...
    plan = models.CharField(max_length=20, choices=[("free", "Free"), ("pro", "Pro")], default="free")
    stripe_subscription_id = models.CharField(max_length=255, blank=True, null=True)
