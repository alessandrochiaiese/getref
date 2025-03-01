
from django.shortcuts import get_object_or_404, redirect, render
from subscriptions.models.promotion import Promotion
from subscriptions.models.promotion_sale import PromotionSale

import stripe
from subscriptions.views.views_subscription import get_prices_for_product


def my_promotions(request):
    # Recupera tutte le promozioni per l'utente autenticato
    promotions = Promotion.objects.filter(user=request.user)
    
    # Recupera i dettagli dei prodotti Stripe per ogni promozione
    products = []
    for promotion in promotions:
        try:
            product = stripe.Product.retrieve(promotion.stripe_product_id)
            products.append({
                'promotion': promotion,
                'product': product
            })
        except stripe.error.StripeError as e:
            # Gestisci gli errori di Stripe, come la mancata connessione o errore nell'ID del prodotto
            print(f"Errore nel recupero del prodotto Stripe per la promozione {promotion.id}: {e}")

    # Passa le promozioni e i dettagli dei prodotti al template
    return render(request, 'promotions/my_promotions.html', {'products': products})

def promote(request, promotion_link):
    # Ottieni la promozione tramite il link
    promotion = get_object_or_404(Promotion, promotion_link=promotion_link)
    
    # Recupera il prodotto Stripe utilizzando l'ID del prodotto
    product = stripe.Product.retrieve(promotion.stripe_product_id)
    
    # Crea una sessione di checkout con Stripe
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': product.name or 'Product Promotion',  # Puoi personalizzare qui il nome del prodotto
                },
                'unit_amount': 2000,  # Prezzo in centesimi (es. $20)
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/success/'),
        cancel_url=request.build_absolute_uri('/cancel/'),
    )

    # Reindirizza direttamente alla sessione di checkout di Stripe
    return redirect(checkout_session.url)

def promote_bak(request, promotion_link):
    # Ottieni la promozione tramite il link
    promotion = get_object_or_404(Promotion, promotion_link=promotion_link)
    product = stripe.Product.list(product=promotion['stripe_product_id'])
    # Crea una sessione di checkout con Stripe
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': product.name or 'Product Promotion',  # Puoi personalizzare qui il nome del prodotto
                },
                'unit_amount': 2000,  # Prezzo in centesimi (es. $20)
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/success/'),
        cancel_url=request.build_absolute_uri('/cancel/'),
    )

    # Restituisce il link di Stripe per il pagamento
    return render(request, 'promotions/promotion_checkout.html', {
        'checkout_session_id': checkout_session.id
    })

def promotion_sales(request):
    # Recupera tutte le vendite promozionali per l'utente
    sales = PromotionSale.objects.filter(promotion__user=request.user)
    return render(request, 'promotions/promotion_sales.html', {'sales': sales})
