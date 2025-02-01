from django.db import models

class APIUsageLog(models.Model):
    api_key = models.CharField(max_length=255)
    endpoint = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.api_key} - {self.endpoint} at {self.timestamp}"
