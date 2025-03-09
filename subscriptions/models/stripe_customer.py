from django.contrib.auth.models import User
from django.db import models

class StripeCustomer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stripeCustomerId = models.CharField(default=None, null=True, max_length=255)
    stripeSubscriptionId = models.CharField(default=None, null=True, max_length=255)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'stripe_customers'
        verbose_name = 'StripeCustomer'
        verbose_name_plural = 'StripeCustomers'
