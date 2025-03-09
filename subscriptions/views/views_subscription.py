#DOMAIN='https://affiliate.getcall.it'
import datetime
from getref.settings import DOMAIN
import stripe
from getref import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

from referral.models import *
from subscriptions.models import *

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def test(request):
    try:
        # Retrieve the subscription & product
        stripe_customer = StripeCustomer.objects.get(user=request.user)
        # load stipe secret key here
        subscription = stripe.Subscription.retrieve(stripe_customer.stripeSubscriptionId)
        product = stripe.Product.retrieve(subscription.plan.product)

        # Feel free to fetch any additional data from 'subscription' or 'product'
        # https://stripe.com/docs/api/subscriptions/object
        # https://stripe.com/docs/api/products/object

        return render(request, 'subscriptions/test.html', {
            'subscription': subscription,
            'product': product,
        })

    except StripeCustomer.DoesNotExist:
        return render(request, 'subscriptions/test.html')

def get_products_paid(user):
    purchased_one_time_products = []
    # Recupera il cliente Stripe per l'utente
    #stripe_customers = StripeCustomer.objects.filter(user=user, stripeSubscriptionId="" or None).all()
    one_time_purchases = OneTimePurchase.objects.filter(stripe_customer__user=user).all()

    if one_time_purchases:
        #for stripe_customer in stripe_customers:
            
        for one_time_purchase in one_time_purchases:
            product_id = one_time_purchase.product_id
            product = stripe.Product.retrieve(product_id)
            prices = get_prices_for_product(product_id)
            purchased_one_time_products.append({
                'name': product.name,
                'id': product.id,
                'description': product.description,
                'price_amount': prices[0]['price_amount'] or prices['price_amount'],
                'amount': 1, #product['unit_amount'] / 100,  # Converti da cent a euro
                'currency': 'EUR' #str(price['currency']).upper(),
            })
        print("purchased_one_time_products: ", purchased_one_time_products)
        return purchased_one_time_products
    return []

def get_subscription_plan_paid(user):
    subscriptions = []
    # Recupera il cliente Stripe per l'utente
    stripe_customers = StripeCustomer.objects.filter(user=user).all()
    
    if stripe_customers:
        for stripe_customer in stripe_customers:
            # load stipe secret key here
            subscription = stripe.Subscription.retrieve(stripe_customer.stripeSubscriptionId)
            product = stripe.Product.retrieve(subscription.plan.product)
            prices = get_prices_for_product(product)
            subscriptions.append({
                'status': subscription.status,
                'price_amount': prices[0]['price_amount'] or prices['price_amount'],
                'currency': str(prices[0]['currency'] or prices['price_amount']).upper() or 'EUR',
                'name': product.name,
                'description': product.description,

            })

        return subscriptions    
    return []  


@login_required
def plans(request):
    try:        
        # Retrieve all available products
        all_products = list_stripe_all_products()
        
        # Retrieve all available plans
        products = list_plans(all_products)

        # Recupera tutte le sottoscrizioni dell'utente
        subscriptions = get_subscription_plan_paid(request.user) or []
                    

        return render(request, 'subscriptions/plans.html', {
            'subscriptions': subscriptions,
            'products': products,  # Pass the list of products to the template
        })


    except stripe.error.StripeError as e:
        print(f"Errore Stripe: {str(e)}")  # Log di errore Stripe
        pass
    except Exception as e:
        print(f"Errore generico: {str(e)}")  # Log di errore generico
        pass
    except StripeCustomer.DoesNotExist:
        # If the user doesn't have an active subscription
        pass

    return render(request, 'subscriptions/plans.html', {
        'products': products,
    })


@login_required
def products(request):
    try:
        # Recupera tutti i prodotti da Stripe
        products = list_stripe_all_products()

        # Filtra i prodotti 'one-time'
        one_time_products = list_products(products)

        return render(request, 'subscriptions/products.html', {
            'one_time_products': one_time_products,  # Passa i prodotti one-time
        })
    except Exception as e:
        print(f"Errore recuperando i prodotti: {str(e)}")
        return render(request, 'subscriptions/products.html', {
            'one_time_products': [],
        })

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

# Funzione per recuperare i prodotti e i prezzi da Stripe
def list_stripe_all_products():
    try:
        print("Tentativo di recuperare i prodotti da Stripe...")  # Aggiungi log per il debug
        products = stripe.Product.list()

        product_list = []

        for product in products.auto_paging_iter():
            # Recupera i prezzi associati al prodotto
            prices = stripe.Price.list(product=product.id)

            for price in prices.auto_paging_iter():
                product_list.append({
                    'product_name': product.name,
                    'product_id': product.id,
                    'price_id': price.id,
                    'price_amount': str(round(price.unit_amount / 100, 2)),
                    'currency': price.currency,
                    'billing_scheme': price.billing_scheme,
                    'type': price.type
                })
        
        print(f"Prodotti recuperati: {product_list}")  # Log per vedere i prodotti recuperati
        return product_list
    except stripe.error.StripeError as e:
        print(f"Errore Stripe: {str(e)}")  # Log di errore Stripe
        return {'error': f"Stripe Error: {str(e)}"}
    except Exception as e:
        print(f"Errore generico: {str(e)}")  # Log di errore generico
        return {'error': str(e)}

def list_products(products):
    product_list = []
    for product in products:
        if product.get('type') == 'one_time':
            product_list.append(product)
    return product_list

"""def list_plans(products):
    product_list = []
    for product in products:
        if product.get('type') == 'recurring': # 'recurring
            product_list.append(product)
    return product_list
"""

def list_plans(products):
    product_list = []
    for product in products:
        # Recupera i prezzi associati al prodotto
        prices = stripe.Price.list(product=product['product_id'])

        for price in prices.auto_paging_iter():
            if price.billing_scheme == 'tiered' or price.recurring or product.get('type') == 'recurring':  # Verifica se è ricorrente
                product_list.append({
                    'product_name': product['product_name'],
                    'product_id': product['product_id'],
                    'price_id': price.id,
                    'price_amount': str(round(price.unit_amount / 100, 2)),
                    'currency': price.currency,
                    'billing_scheme': price.billing_scheme,
                    'type': price.type,
                    'interval': price.recurring.interval if price.recurring else None  # Intervallo ricorrente
                })
                break  # Se abbiamo trovato un piano ricorrente, non è necessario continuare con gli altri prezzi dello stesso prodotto
    return product_list

def get_product_by_price_id(products, price_id):
    return next((product for product in products if product['price_id'] == price_id), None)

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        # load stipe secret key here
        price_id = request.GET.get('priceId')
        promotion_link = request.GET.get('promotionLink')

        try:
            print("Recupero dei prodotti e dei prezzi...")  # Log for debugging
            products = list_stripe_all_products()
            #plans = list_plans(products)            

            if not products:
                print("Nessun prodotto trovato in Stripe.") 
                return JsonResponse({'error': 'No products found in Stripe.'}, status=404)

            if not price_id:
                return JsonResponse({'error': 'No price ID found.'}, status=400)
            
            selected_product = get_product_by_price_id(products, price_id)
            print('Product selected: ', selected_product)
            
            if selected_product and selected_product.get('type') == 'recurring' and selected_product.get('type') != 'one_time':
                mode = 'subscription'
            elif selected_product and selected_product.get('type') == 'one_time' and selected_product.get('type') != 'recurring':
                mode = 'payment'

            metadata = {}
            if promotion_link:
                metadata={
                    'promotion_link': promotion_link
                },
            
            # Create checkout session
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=f"{DOMAIN}/success?session_id={{CHECKOUT_SESSION_ID}}",
                cancel_url=f"{DOMAIN}/cancel/",
                payment_method_types=['card'],
                mode= mode, # 'subscription' if price is recurring type else 'payment'
                line_items=[{
                    'price': price_id,
                    'quantity': 1,
                }],
                metadata=metadata,
                customer_creation='always',  # "if_required" # Forza sempre la creazione del cliente
                customer_email=request.user.email if request.user.is_authenticated else None  # Imposta l'email
            )

            return JsonResponse({'sessionId': checkout_session.id})

        except stripe.error.StripeError as e:
            return JsonResponse({'error': f"Stripe Error: {str(e)}"}, status=500)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

def get_prices_for_product(product_id):
    try:
        # Recupera i prezzi associati al prodotto
        prices = stripe.Price.list(product=product_id)
        price_list = []

        for price in prices.auto_paging_iter():
            price_list.append({
                'price_id': price.id,
                'price_amount': str(round(price.unit_amount / 100, 2)),
                #'amount': price.unit_amount / 100,  # Converti da centesimi a unità di valuta
                'currency': price.currency.upper(),
                'billing_scheme': price.billing_scheme,
                'type': price.type
            })
        
        return price_list

    except stripe.error.StripeError as e:
        print(f"Errore Stripe: {str(e)}")
        return {'error': f"Stripe Error: {str(e)}"}
    except Exception as e:
        print(f"Errore generico: {str(e)}")
        return {'error': str(e)}

@login_required
def purchased_products(request):
    try:
        purchased_one_time_products = get_products_paid(request.user) or []
        
        # Passa i dati al template
        return render(request, 'subscriptions/purchased_products.html', {
            'purchased_one_time_products': purchased_one_time_products,  # Prodotti one-time acquistati
        })
    
    except stripe.error.StripeError as e:
        print(f"Errore Stripe: {str(e)}")  # Log di errore Stripe
        pass
    except Exception as e:
        print(f"Errore generico: {str(e)}")  # Log di errore generico
        pass
    except StripeCustomer.DoesNotExist:
        # If the user doesn't have an active subscription
        pass

    return render(request, 'subscriptions/purchased_products.html', {
        'purchased_one_time_products': [],
    })


@login_required
def success(request):
    return render(request, 'subscriptions/success.html')


@login_required
def cancel(request):
    return render(request, 'subscriptions/cancel.html')

def check_for_reward(user):
    number_of_customer_seller = 0
    
    # Seller get Bonus if more than 5 customer have made first bought
    referrals = Referral.objects.filter(referrer=user).all()
    if referrals.count() >=5:
        for referral in referrals:
            promotion_sales = PromotionSale.objects.filter(user=referral.referred).all()
            one_time_purchases = OneTimePurchase.objects.filter(stripe_customer__user=referral.referred).all()
            if promotion_sales.count() + one_time_purchases.count() >= 1:
                number_of_customer_seller += 1

        if number_of_customer_seller >= 5:
            referral_code = ReferralCode.objects.filter(user=user).first()
            referral_reward = ReferralReward.objects.create(
                referral_code=referral_code,
                user=user,
                reward_type="Cash",
                reward_value=50.00,
                date_awarded=datetime.datetime.now(),
                status="Awarded",
                expiry_date=datetime.datetime.today() + datetime.timedelta(days=30),
                reward_description="Premio per aver completato la registrazione",
                reward_source="ReferralProgram"
            )
            referral_notification = ReferralNotification.objects.create(
                user=user,
                message="Hai ricevuto un nuovo referral bonus!",
                date_sent=datetime.datetime.now(),
                is_read=False,
                notification_type="Bonus",
                priority="High",
                action_required=True
            )


@csrf_exempt
def stripe_webhook(request):
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        print(session)
        # Retrieve metadata from the session
        client_reference_id = session.get('client_reference_id')
        # Ottieni l'ID della sessione
        session_id = session.get('id')

        # Recupera la sessione completa usando l'ID della sessione
        checkout_session = stripe.checkout.Session.retrieve(session_id)

        # Ottieni il customer dalla sessione
        mode = checkout_session.get('mode')
        stripe_customer_id = checkout_session.get('customer', None)
        stripe_subscription_id = checkout_session.get('subscription', None)  # Questo può essere null se il checkout non è per una sottoscrizione

        print("mode: ", mode)
        print("stripe_customer_id: ", stripe_customer_id)
        print("stripe_subscription_id: ", stripe_subscription_id)
        #stripe_customer_id = session.get('stripe_customer_id')
        #stripe_subscription_id = session.get('stripe_subscription_id')

        try:
            # Log per il debug
            print(f"Received session for user ID {client_reference_id}, customer ID {stripe_customer_id}, subscription ID {stripe_subscription_id}")

            user = User.objects.get(id=client_reference_id)  # Trova l'utente
            referral_code = ReferralCode.objects.get(user=user)

            # Handle subscription and one-time payments
            if mode == 'subscription':
                # Verifica se il customer esiste o lo crea
                stripe_customer = StripeCustomer.objects.create(
                    user=user,
                    stripeCustomerId=stripe_customer_id,
                    stripeSubscriptionId=stripe_subscription_id
                )

                # Verifica che i valori non siano nulli
                if not stripe_customer_id: # or not stripe_subscription_id:
                    print(f"Error: Missing customer ID. session: {session}")
                    #print(f"Error: Missing customer ID or subscription ID. session: {session}")
                    return HttpResponse(status=400)

                # Subscription created, save the subscription details
                stripe_subscription = stripe.Subscription.retrieve(stripe_subscription_id)
                product = stripe.Product.retrieve(stripe_subscription.plan.product) #BUG: Error while processing Stripe webhook: 'str' object has no attribute 'name'
                prices = get_prices_for_product(product)
                    
                subscription = StripeSubscription.objects.create(
                    stripe_customer=stripe_customer,
                    stripe_subscription_id=stripe_subscription_id,
                    product_name=product.name,#BUG: Error while processing Stripe webhook: 'str' object has no attribute 'name'
                    product_id=stripe_subscription.plan.product,
                    status=stripe_subscription.status
                )
                print(f"Subscription saved for {user.username}.")
                ReferralTransaction(
                    referral_code = referral_code,
                    referred_user = user,
                    transaction_date = datetime.datetime.now(),
                    order = None,
                    transaction_amount = price_amount,
                    currency = currency,
                    status = 'completed',
                    conversion_value = 2,
                    discount_value = 0,
                    coupon_code_used = "",
                    channel = ""
                )
            elif mode == 'payment':
                #payment_intent_id = checkout_session.get('payment_intent')  # Assicurati che ci sia un payment_intent
                #payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)
                #print(f"payment_intent: {payment_intent}")
                #stripe_customer_id = payment_intent.get('customer', "")
                stripe_customer = StripeCustomer.objects.create(
                    user=user,
                    stripeCustomerId=stripe_subscription_id,
                    stripeSubscriptionId=stripe_subscription_id
                )

                print(f"Using StripeCustomer for user {user.username}.")

                # Handle one-time payment (if no subscription ID is available)
                line_items = stripe.checkout.Session.list_line_items(session_id)
                line_item = line_items.data[0] if line_items.data else None
                print("line_item: ", line_item)
                """if not line_item:
                    print(f"Error: No line items found for session {session_id}")
                    return HttpResponse(status=400)
                """
                #line_item = checkout_session.get('line_items')['data'][0]  # Get the first line item
                one_time_product_name = line_item.get('description')
                one_time_product_id = line_item.get('price').get('product')
                price_amount = line_item.get('amount_total') / 100.0  # Convert cents to dollars/euros
                currency = line_item.get('currency').upper()

                # Save the one-time purchase
                one_time_purchase = OneTimePurchase.objects.create(
                    stripe_customer=stripe_customer,
                    product_name=one_time_product_name,
                    product_id=one_time_product_id,
                    price_amount=price_amount,
                    currency=currency,
                    status='completed'
                )
                print(f"One-time purchase saved for {user.username}.")

                ReferralTransaction(
                    referral_code = referral_code,
                    referred_user = user,
                    transaction_date = datetime.datetime.now(),
                    order = None,
                    transaction_amount = prices[0]['price_amount'] or prices['price_amount'],
                    currency = prices[0]['currency'] or prices['currency'],
                    status = 'completed',
                    conversion_value = 2,
                    discount_value = 0,
                    coupon_code_used = "",
                    channel = ""
                )
            # Se il prodotto è stato promosso da un venditore
            promotion_link = session.get('metadata', {}).get('promotion_link')
            ReferralTransaction.objects.create()
            if promotion_link:
                promotion = Promotion.objects.filter(promotion_link=promotion_link).first()
                if promotion:
                    # Crea una nuova vendita promozionale
                    PromotionSale.objects.create(
                        promotion=promotion,
                        user=promotion.user,  # Assumiamo che l'utente che ha creato la promozione sia il venditore
                        amount=session['amount_total'] / 100,  # Prezzo in dollari
                    )
                customer = request.user
                seller = promotion.user
                check_for_reward(user)

        except Exception as e:
            print(f"Error while processing Stripe webhook: {str(e)}")
            return HttpResponse(status=400)

    return HttpResponse(status=200)

    """
    Current Errors:
    Bad Request: /webhook/
    Received session for user ID 1, customer ID None, subscription ID None
    Error while processing Stripe webhook: null value in column "stripeCustomerId" of relation "stripe_customers"
    DETAIL:  Failing row contains (25, null, null, 1).
     "POST /webhook/ HTTP/1.0" 400 0 
     
    """