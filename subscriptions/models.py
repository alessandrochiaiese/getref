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



class StripeSubscription(models.Model):
    stripe_customer = models.ForeignKey(StripeCustomer, on_delete=models.CASCADE, related_name='subscriptions')
    stripe_subscription_id = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    product_id = models.CharField(max_length=255)
    status = models.CharField(max_length=50)  # Active, past_due, canceled, etc.
    subscription_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Subscription to {self.product_name} ({self.status})"
    
    class Meta:
        db_table = 'stripe_subscriptions'
        verbose_name = 'StripeSubscription'
        verbose_name_plural = 'StripeSubscriptions'

