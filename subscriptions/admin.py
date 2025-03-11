from django.contrib import admin
from subscriptions.models import *

#admin.site.register(StripeCustomer)
#admin.site.register(Subscription)
admin.site.register(OneTimePurchase)
admin.site.register(Plan)
admin.site.register(Promotion)
admin.site.register(PromotionSale)
#admin.site.register(APIKey)
#admin.site.register(APIUsageLog)

@admin.register(StripeCustomer)
class StripeCustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'stripeCustomerId', 'stripeSubscriptionId')
    search_fields = ('user__username', 'stripeCustomerId')  # Aggiungi un campo per cercare per nome utente

@admin.register(StripeSubscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('stripe_customer', 'product_name', 'status', 'subscription_date')
    search_fields = ('stripe_customer__user__username', 'product_name', 'status')
    list_filter = ('status', 'stripe_customer')

@admin.register(APIKey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'created_at', 'last_used_at', 'request_count', 'plan')  # Aggiungi i campi corretti
    search_fields = ('client_id', 'plan')  # Puoi anche aggiungere campi per la ricerca
    list_filter = ('plan',)  # Permette di filtrare per piano

@admin.register(APIUsageLog)
class APIUsageLogAdmin(admin.ModelAdmin):
    list_display = ('api_key', 'endpoint', 'timestamp')
    list_filter = ('timestamp',)  # Puoi filtrare anche per timestamp
