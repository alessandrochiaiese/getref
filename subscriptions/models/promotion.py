from django.db import models
from django.contrib.auth.models import User
import uuid

from getref.settings import DOMAIN

class Promotion(models.Model):
    stripe_product_id = models.CharField(max_length=255)  # ID del prodotto Stripe
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # L'utente che promuove il prodotto
    promotion_link = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Link unico per la promozione
    created_at = models.DateTimeField(auto_now_add=True)

    def get_promotion_url(self):
        return f"{DOMAIN}/promote/{self.promotion_link}"
