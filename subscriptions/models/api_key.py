from oauth2_provider.models import Application
from django.db import models
from django.utils.timezone import now

class APIKey(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_used_at = models.DateTimeField(null=True, blank=True)
    request_count = models.PositiveIntegerField(default=0)
    plan = models.CharField(max_length=20, choices=[("free", "Free"), ("pro", "Pro")], default="free")
    stripe_subscription_id = models.CharField(max_length=255, blank=True, null=True)
    client_id = models.CharField(max_length=255, blank=True, null=True, unique=True)  # Aggiunta di un client ID

    def update_usage(self):
        if not self.stripe_subscription_id or not self.plan:
            raise ValueError("API Key non associata a una sottoscrizione valida.")
        self.last_used_at = now()
        self.request_count += 1
        self.save()

    def __str__(self):
        return f"{self.client_id} ({self.plan})"


"""
# subscriptions/models/api_key.py
from django.db import models

class APIKey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client_id = models.CharField(max_length=100)
    client_secret = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

"""