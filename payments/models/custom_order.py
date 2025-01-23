from django.urls import reverse
from getref import settings
from django.db import models 

from django.contrib.auth.models import User

class CustomOrder(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=8)
    description = models.CharField(max_length=128)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('order-detail', kwargs={"pk": self.pk})

    def get_total_amount(self):
        return self.amount

    def get_buyer_info(self):
        return {"email": self.buyer.email}

    def get_currency(self):
        return "EUR"

    def get_description(self):
        return self.description