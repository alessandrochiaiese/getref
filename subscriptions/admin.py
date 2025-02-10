from django.contrib import admin
from subscriptions.models import StripeCustomer, Subscription


admin.site.register(StripeCustomer)
admin.site.register(Subscription)
