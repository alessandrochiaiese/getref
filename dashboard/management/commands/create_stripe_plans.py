import json
import stripe
from django.core.management.base import BaseCommand
from django.conf import settings

# Impostazione della chiave API Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

PLANS = {
  "subscriptions": [
    {
      "id": "affiliate-basic",
      "name": "Affiliate System - Base",
      "description": "Accesso base al sistema di affiliazione con funzionalità limitate.",
      "price": 2900,
      "currency": "EUR",
      "interval": "month",
      "metadata": {
        "features": "Dashboard affiliato: ✔, Monitoraggio commissioni: ✔, Pagamenti mensili: ✔, Integrazione API: ❌, Tracciamento in tempo reale: ❌, Supporto: Email",
        "rate_limit": "max_api_calls_per_day: 100, max_affiliates: 50"
      }
    },
    {
      "id": "affiliate-pro",
      "name": "Affiliate System - Pro",
      "description": "Piano avanzato con più funzionalità e integrazione API.",
      "price": 5900,
      "currency": "EUR",
      "interval": "month",
      "metadata": {
        "features": "Dashboard affiliato: ✔, Monitoraggio commissioni: ✔, Pagamenti settimanali: ✔, Integrazione API: ✔, Tracciamento in tempo reale: ✔, Supporto: Email e Chat",
        "rate_limit": "max_api_calls_per_day: 1000, max_affiliates: 200"
      }
    },
    {
      "id": "affiliate-premium",
      "name": "Affiliate System - Premium",
      "description": "Piano completo con tutte le funzionalità, inclusi pagamenti giornalieri e supporto premium.",
      "price": 9900,
      "currency": "EUR",
      "interval": "month",
      "metadata": {
        "features": "Dashboard affiliato: ✔, Monitoraggio commissioni: ✔, Pagamenti giornalieri: ✔, Integrazione API: ✔, Tracciamento in tempo reale: ✔, Strumenti di marketing: ✔, Supporto: Email, Chat e Telefono",
        "rate_limit": "max_api_calls_per_day: Illimitato, max_affiliates: Illimitato"
      }
    },
    
      {
        "id": "referral-basic",
        "name": "Referral Code System - Base",
        "description": "Sistema di referral base con tracciamento e gestione delle ricompense.",
        "price": 2900,
        "currency": "EUR",
        "interval": "month",
        "metadata": {
            "features": "Generazione codici referral: ✔, Tracciamento conversioni: ✔, Gestione ricompense: ✔, Reportistica avanzata: ❌, Personalizzazione ricompense: ❌, Supporto: Email",
            "rate_limit": "max_referral_codes: 100, max_referral_uses_per_month: 500"
          
        }
      },
      {
        "id": "referral-pro",
        "name": "Referral Code System - Pro",
        "description": "Piano avanzato con più strumenti di gestione referral.",
        "price": 5900,
        "currency": "EUR",
        "interval": "month",
        "metadata": {
          "features": "Generazione codici referral: ✔, Tracciamento conversioni: ✔, Gestione ricompense: ✔, Reportistica avanzata: ✔, Personalizzazione ricompense: ✔, Supporto: Email e Chat",
          "rate_limit": "max_referral_codes: 500, max_referral_uses_per_month: 5000"

        }
      },
      {
        "id": "referral-premium",
        "name": "Referral Code System - Premium",
        "description": "Piano completo con funzionalità avanzate per referral marketing personalizzato.",
        "price": 9900,
        "currency": "EUR",
        "interval": "month",
        "metadata": {
          "features": "Generazione codici referral: ✔, Tracciamento conversioni: ✔, Gestione ricompense: ✔, Reportistica avanzata: ✔, Personalizzazione ricompense: ✔, Campagne personalizzate: ✔, Analisi avanzate: ✔, Supporto: Email, Chat e Telefono",
          "rate_limit": "max_referral_codes: Illimitato, max_referral_uses_per_month: Illimitato"
          
        }
      }
  ]
}

class Command(BaseCommand):
    help = 'Crea i prodotti, i prezzi e i piani su Stripe a partire dai dati di plans.json'

    def handle(self, *args, **kwargs):
        # Caricamento dei dati dei piani dal file JSON
        data_plans = PLANS
        subscriptions = data_plans.get('subscriptions', [])

        for subscription_data in subscriptions:
            try:
                # 1. Creazione del prodotto su Stripe
                product = stripe.Product.create(
                    name=subscription_data['name'],
                    description=subscription_data['description'],
                    metadata=subscription_data['metadata'],
                )

                # 2. Creazione del prezzo associato al prodotto su Stripe
                price = stripe.Price.create(
                    product=product.id,  # Associa il prezzo al prodotto appena creato
                    unit_amount=subscription_data['price'],
                    currency=subscription_data['currency'],
                    recurring={'interval': subscription_data['interval']},  # Prezzo ricorrente (mensile)
                    metadata=subscription_data['metadata'],
                )

                # 3. Creazione del piano: L'oggetto prezzo è ciò che costituisce il piano!
                # In Stripe, il "piano" è il "prezzo" associato al prodotto. Quindi non c'è bisogno di creare un "piano" separato.
                self.stdout.write(self.style.SUCCESS(f"Piano '{subscription_data['name']}' creato con successo. ID prodotto: {product.id}, ID prezzo: {price.id}"))
                
            except stripe.error.StripeError as e:
                self.stdout.write(self.style.ERROR(f"Errore nella creazione del piano '{subscription_data['name']}': {e}"))
