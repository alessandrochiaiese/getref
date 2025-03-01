import json
import stripe
from django.core.management.base import BaseCommand
from django.conf import settings

# Impostazione della chiave API Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

PRODUCTS ={
  "products": [
    {
      "id": "course-sales",
      "name": "Corso di formazione per venditori",
      "description": "Un corso completo per migliorare le tecniche di vendita, dalla comunicazione persuasiva alla chiusura delle trattative.",
      "price": 19900,
      "currency": "EUR",
      "type": "one_time",
      "metadata": {
        "category": "Formazione",
        "level": "Intermedio",
        "duration": "6 settimane",
        "access": "Illimitato",
        "format": "Video lezioni, PDF, Esercizi pratici",  # Modifica qui, unisci gli array in una stringa
        "features": "Tecniche di vendita avanzate: ✔, Gestione delle obiezioni: ✔, Negoziazione e chiusura contratti: ✔, Sessioni live con esperti: ❌, Certificato di completamento: ✔"  # Modifica anche qui
      }
    },
    {
      "id": "course-pnl",
      "name": "Corso di formazione PNL",
      "description": "Impara le tecniche della Programmazione Neuro-Linguistica per la crescita personale e professionale.",
      "price": 24900,
      "currency": "EUR",
      "type": "one_time",
      "metadata": {
        "category": "Formazione",
        "level": "Avanzato",
        "duration": "8 settimane",
        "access": "Illimitato",
        "format": "Video lezioni, Esercizi pratici, Webinar",  # Unisci gli array in una stringa
        "features": "Introduzione alla PNL: ✔, Tecniche di persuasione: ✔, Miglioramento delle relazioni interpersonali: ✔, Sessioni live con coach: ✔, Certificato di completamento: ✔"  # Stringa formattata
      }
    },
    {
      "id": "course-seo",
      "name": "Corso di formazione SEO",
      "description": "Un corso completo per imparare le strategie di ottimizzazione per i motori di ricerca.",
      "price": 29900,
      "currency": "EUR",
      "type": "one_time",
      "metadata": {
        "category": "Formazione",
        "level": "Esperto",
        "duration": "10 settimane",
        "access": "1 anno",
        "format": "Video lezioni, PDF, Esercizi pratici, Sessioni live",  # Unisci gli array in una stringa
        "features": "Fondamenti SEO: ✔, SEO on-page e off-page: ✔, SEO tecnica e velocità del sito: ✔, Keyword research avanzata: ✔, Strumenti SEO (Google Search Console, SEMrush, Ahrefs): ✔, Sessioni live con esperti SEO: ✔, Certificato di completamento: ✔"  # Stringa formattata
      }
    }
  ]
}

class Command(BaseCommand):
    help = 'Crea i prodotti su Stripe a partire dai dati di products.json'

    def handle(self, *args, **kwargs):
        # Caricamento dei dati dei prodotti dal file JSON
        #with open('path/to/your/products.json') as f:
        #    data = json.load(f)

        data = PRODUCTS
        products = data.get('products', [])

        for product_data in products:
            try:
                # Creazione del prodotto su Stripe
                product = stripe.Product.create(
                    id=product_data['id'],
                    name=product_data['name'],
                    description=product_data['description'],
                    metadata=product_data['metadata'],
                )
                # Creazione del prezzo associato al prodotto su Stripe
                stripe.Price.create(
                    product=product.id,
                    unit_amount=product_data['price'],
                    currency=product_data['currency'],
                    recurring=None if product_data['type'] == 'one_time' else {'interval': 'month'},
                )
                self.stdout.write(self.style.SUCCESS(f"Prodotto '{product_data['name']}' creato con successo."))
            except stripe.error.StripeError as e:
                self.stdout.write(self.style.ERROR(f"Errore nella creazione del prodotto '{product_data['name']}': {e}"))
