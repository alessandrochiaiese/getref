from django.contrib.auth.models import User
from django.db import models

class StripeSubscription(models.Model):
    stripe_customer = models.ForeignKey('StripeCustomer', on_delete=models.CASCADE, related_name='subscriptions')
    stripe_subscription_id = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    product_id = models.CharField(max_length=255)
    status = models.CharField(max_length=50)  # Active, past_due, canceled, etc.
    subscription_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Subscription to {self.product_name} ({self.status})"
    
    class Meta:
        db_table = 'custom_stripe_subscriptions'
        verbose_name = 'StripeSubscription'
        verbose_name_plural = 'StripeSubscriptions'
