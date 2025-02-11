from django.contrib import admin
from subscriptions.models import StripeCustomer, StripeSubscription


#admin.site.register(StripeCustomer)
#admin.site.register(Subscription)

# Registra il modello StripeCustomer
@admin.register(StripeCustomer)
class StripeCustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'stripeCustomerId', 'stripeSubscriptionId')
    search_fields = ('user__username', 'stripeCustomerId')  # Aggiungi un campo per cercare per nome utente


"""@admin.register(StripeSubscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('stripe_customer', 'product_name', 'status', 'subscription_date')
    search_fields = ('stripe_customer__user__username', 'product_name', 'status')
    list_filter = ('status', 'stripe_customer')"""
admin.site.register(StripeSubscription) #, SubscriptionAdmin)
