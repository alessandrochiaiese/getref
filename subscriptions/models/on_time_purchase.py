from django.contrib.auth.models import User
from django.db import models

class OneTimePurchase(models.Model):
    user = models.ForeignKey(User, default=None, null=True, on_delete=models.CASCADE, related_name="buyer")
    product_name = models.CharField(max_length=255)  # Nome del prodotto acquistato
    product_id = models.CharField(max_length=255)  # ID del prodotto da Stripe
    price_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Prezzo del prodotto
    currency = models.CharField(max_length=10)  # Valuta (ad esempio USD, EUR)
    status = models.CharField(max_length=50, default='completed')  # Stato del pagamento, per esempio 'completed'
    purchased_at = models.DateTimeField(auto_now_add=True)  # Data di acquisto

    def __str__(self):
        return f"Purchase of {self.product_name} by {self.stripe_customer.user.username}"
