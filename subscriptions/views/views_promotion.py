
from django.shortcuts import get_object_or_404, render
from subscriptions.models.promotion import Promotion
from subscriptions.models.promotion_sale import PromotionSale

import stripe

def my_promotions(request):
    # Recupera tutte le promozioni per l'utente autenticato
    promotions = Promotion.objects.filter(user=request.user)

    # Passa le promozioni al template
    return render(request, 'promotions/my_promotions.html', {'promotions': promotions})

def promote(request, promotion_link):
    # Ottieni la promozione tramite il link
    promotion = get_object_or_404(Promotion, promotion_link=promotion_link)

    # Crea una sessione di checkout con Stripe
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'Product Promotion',  # Puoi personalizzare qui il nome del prodotto
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
