
import datetime
from urllib.parse import urlencode
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from referral.models.referral import Referral
from referral.models.referral_bonus import ReferralBonus
from referral.models.referral_code import ReferralCode
from referral.models.referral_notification import ReferralNotification
from referral.models.referral_reward import ReferralReward
from subscriptions.models.on_time_purchase import OneTimePurchase
from subscriptions.models.promotion import Promotion
from subscriptions.models.promotion_sale import PromotionSale

import stripe
from subscriptions.views.views_subscription import check_for_reward, get_prices_for_product


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

@login_required
def promote(request):
    promotion_link = request.GET.get('code')
    # Costruisci l'URL con il parametro di query
    url = reverse('create_checkout_session')  # Ottieni la base dell'URL
    query_string = urlencode({'promotionLink': promotion_link})  # Aggiungi il parametro alla query
    full_url = f'{url}?{query_string}'  # Combina l'URL con la query

    return HttpResponseRedirect(full_url)

@login_required
def promote_test(request, promotion_link):
    # Ottieni la promozione tramite il link
    promotion = get_object_or_404(Promotion, promotion_link=promotion_link)
    
    # Recupera il prodotto Stripe utilizzando l'ID del prodotto
    product = stripe.Product.retrieve(promotion.stripe_product_id)
    prices = get_prices_for_product(product)
    #price = float(prices[0]['price_amount'] or prices['price_amount'])
    customer = request.user
    seller = promotion.user

    customer_rewards = ReferralReward.objects.filter(user=customer).all()
    
    # Seller get Commission
    #unit_commission = prices[0]['price_amount'] or prices['price_amount'] * 0.15
    #unit_amount = prices[0]['price_amount'] or prices['price_amount'] - unit_commission #AttributeError: 'list' object has no attribute 'amount'. Did you mean: 'count'?
    # check if customer have bonus
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
        success_url=request.build_absolute_uri('/success/'), #promote/success/
        cancel_url=request.build_absolute_uri('/cancel/'),   #promote/cancel/
    )

    check_for_reward(seller)

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
