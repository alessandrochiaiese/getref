from oauth2_provider.models import AbstractApplication
from django.db import models

class CustomApplication(AbstractApplication):
    extra_field = models.CharField(max_length=255, blank=True, null=True)
