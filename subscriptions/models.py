from django.contrib.auth.models import User
from django.db import models


class StripeCustomer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stripeCustomerId = models.CharField(max_length=255)  # Cambia il nome del campo qui
    stripeSubscriptionId = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'stripe_customers'
        verbose_name = 'StripeCustomer'
        verbose_name_plural = 'StripeCustomers'
