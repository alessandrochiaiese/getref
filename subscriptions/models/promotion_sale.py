from django.db import models
from django.contrib.auth.models import User

class PromotionSale(models.Model):
    promotion = models.ForeignKey('Promotion', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    purchased_at = models.DateTimeField(auto_now_add=True)
