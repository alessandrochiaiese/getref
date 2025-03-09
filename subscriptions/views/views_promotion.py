
import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from referral.models.referral import Referral
from referral.models.referral_bonus import ReferralBonus
from referral.models.referral_code import ReferralCode
from referral.models.referral_notification import ReferralNotification
from referral.models.referral_reward import ReferralReward
from subscriptions.models.on_time_purchase import OneTimePurchase
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

@login_required
def promote(request, promotion_link):
    # Ottieni la promozione tramite il link
    promotion = get_object_or_404(Promotion, promotion_link=promotion_link)
    
    # Recupera il prodotto Stripe utilizzando l'ID del prodotto
    product = stripe.Product.retrieve(promotion.stripe_product_id)
    prices = get_prices_for_product(product.id)
    
    customer = request.user
    seller = promotion.user

    customer_rewards = ReferralReward.objects.filter(user=customer).all()
    
    # Seller get Commission
    unit_commission = prices[0]['price_amount'] or prices['price_amount'] * 0.15
    unit_amount = prices[0]['price_amount'] or prices['price_amount'] - unit_commission #AttributeError: 'list' object has no attribute 'amount'. Did you mean: 'count'?
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

    number_of_customer_seller = 0
    
    # Seller get Bonus if more than 5 customer have made first bought
    referrals = Referral.objects.filter(referrer=seller).all()
    if referrals.count() >=5:
        for referral in referrals:
            promotion_sales = PromotionSale.objects.filter(user=referral.referred).all()
            one_time_purchases = OneTimePurchase.objects.filter(stripe_customer__user=referral.referred).all()
            if promotion_sales.count() + one_time_purchases.count() >= 1:
                number_of_customer_seller += 1

        if number_of_customer_seller >= 5:
            referral_code = ReferralCode.objects.filter(user=seller).first()
            referral_reward = ReferralReward.objects.create(
                referral_code=referral_code,
                user=customer,
                reward_type="Cash",
                reward_value=50.00,
                date_awarded=datetime.datetime.now(),
                status="Awarded",
                expiry_date=datetime.datetime.today() + datetime.timedelta(days=30),
                reward_description="Premio per aver completato la registrazione",
                reward_source="ReferralProgram"
            )
            referral_notification = ReferralNotification.objects.create(
                user=customer,
                message="Hai ricevuto un nuovo referral bonus!",
                date_sent=datetime.datetime.now(),
                is_read=False,
                notification_type="Bonus",
                priority="High",
                action_required=True
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
