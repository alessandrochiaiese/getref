#DOMAIN='https://affiliate.getcall.it'
from getref.settings import DOMAIN
import stripe
from getref import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from subscriptions.models import OneTimePurchase, StripeCustomer, StripeSubscription 

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


@login_required
def plans(request):
    try:
        # Retrieve the subscription & product
        stripe_customer = StripeCustomer.objects.get(user=request.user)
        # load stipe secret key here
        subscription = stripe.Subscription.retrieve(stripe_customer.stripeSubscriptionId)
        product = stripe.Product.retrieve(subscription.plan.product)

        # Feel free to fetch any additional data from 'subscription' or 'product'
        # https://stripe.com/docs/api/subscriptions/object
        # https://stripe.com/docs/api/products/object

        # Retrieve all available products
        all_products = list_stripe_all_products()
        
        # Retrieve all available plans
        products = list_plans(all_products)

        return render(request, 'subscriptions/plans.html', {
            'subscription': subscription,
            'product': product,
            'products': products,  # Pass the list of products to the template
        })

    except StripeCustomer.DoesNotExist:
        # If the user doesn't have an active subscription
        products = list_stripe_all_products()
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

def list_plans(products):
    product_list = []
    for product in products:
        if product.get('type') == 'recurring':
            product_list.append(product)
    return product_list


def get_product_by_price_id(products, price_id):
    return next((product for product in products if product['price_id'] == price_id), None)

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        # load stipe secret key here
        price_id = request.GET.get('priceId')

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
            print('is selected the product: ', selected_product)
            mode = 'subscription' if selected_product.get('type') == 'recurring' else 'payment'
            # 
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
                }]
            )

            return JsonResponse({'sessionId': checkout_session.id})

        except stripe.error.StripeError as e:
            return JsonResponse({'error': f"Stripe Error: {str(e)}"}, status=500)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

@login_required
def purchased_products(request):
    try:
        # Recupera il cliente Stripe per l'utente
        stripe_customer = StripeCustomer.objects.get(user=request.user)

        # Recupera tutte le sottoscrizioni dell'utente
        subscriptions = stripe.Subscription.list(customer=stripe_customer.stripeCustomerId, status='active')
        print(f"Subscriptions: {subscriptions}")  # Debug: visualizzare le sottoscrizioni

        # Recupera tutte le sessioni di checkout completate (per i prodotti one-time)
        checkout_sessions = stripe.checkout.Session.list(customer=stripe_customer.stripeCustomerId, status='complete')
        print(f"Checkout Sessions: {checkout_sessions}")  # Debug: visualizzare le sessioni di checkout

        # Lista per i prodotti one-time acquistati
        purchased_one_time_products = []

        # Verifica ogni sessione di checkout per i prodotti acquistati
        for session in checkout_sessions['data']:
            line_items = stripe.checkout.Session.retrieve(session['id']).line_items
            print(f"Line items for session {session.id}: {line_items}")  # Debug: visualizzare i line items della sessione
            for item in line_items['data']:
                # Verifica se il prodotto è one-time (non ha un prezzo ricorrente)
                if 'recurring' not in item['price']:
                    print(f"One-time product found: {item['product']}")  # Debug: visualizzare il prodotto one-time
                    product = stripe.Product.retrieve(item['product'])
                    purchased_one_time_products.append(product)

        # Ora recuperiamo i piani di abbonamento (recurring)
        purchased_subscriptions = []
        for subscription in subscriptions['data']:
            product = stripe.Product.retrieve(subscription['plan']['product'])
            purchased_subscriptions.append({
                'subscription': subscription,
                'product': product,
            })

        # Passa i dati al template
        return render(request, 'subscriptions/purchased_products.html', {
            'subscriptions': purchased_subscriptions,  # Piani ricorrenti
            'purchased_one_time_products': purchased_one_time_products,  # Prodotti one-time acquistati
        })
    
    except StripeCustomer.DoesNotExist:
        return render(request, 'subscriptions/purchased_products.html', {
            'subscriptions': [],
            'purchased_one_time_products': [],
        })
    except Exception as e:
        print(f"Errore recuperando i prodotti acquistati: {str(e)}")
        return render(request, 'subscriptions/purchased_products.html', {
            'subscriptions': [],
            'purchased_one_time_products': [],
        })


@login_required
def success(request):
    return render(request, 'subscriptions/success.html')


@login_required
def cancel(request):
    return render(request, 'subscriptions/cancel.html')


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
        stripe_customer_id = checkout_session.get('customer')
        stripe_subscription_id = checkout_session.get('subscription', '')  # Questo può essere null se il checkout non è per una sottoscrizione

        #stripe_customer_id = session.get('stripe_customer_id')
        #stripe_subscription_id = session.get('stripe_subscription_id')


        # Verifica che i valori non siano nulli
        if not stripe_customer_id or not stripe_subscription_id:
            print(f"Error: Missing customer ID or subscription ID. session: {session}")
            return HttpResponse(status=400)

        try:
            # Log per il debug
            print(f"Received session for user ID {client_reference_id}, customer ID {stripe_customer_id}, subscription ID {stripe_subscription_id}")

            user = User.objects.get(id=client_reference_id)  # Trova l'utente

            # Verifica se il customer esiste o lo crea
            stripe_customer, created = StripeCustomer(
                user=user,
                stripeCustomerId=stripe_customer_id,
                stripeSubscriptionId=stripe_subscription_id,
            )
            stripe_customer.save()

            if created:
                print(f"StripeCustomer for user {user.username} created.")
            else:
                print(f"StripeCustomer for user {user.username} already exists.")

            # Handle subscription and one-time payments
            if stripe_subscription_id != '':
                # Subscription created, save the subscription details
                stripe_subscription = stripe.Subscription.retrieve(stripe_subscription_id)
                subscription = StripeSubscription(
                    stripe_customer=stripe_customer,
                    stripe_subscription_id=stripe_subscription_id,
                    product_name=stripe_subscription.plan.product.name,
                    product_id=stripe_subscription.plan.product.id,
                    status=stripe_subscription.status,
                )
                subscription.save()
                print(f"Subscription saved for {user.username}.")
            else:
                # Handle one-time payment (if no subscription ID is available)
                line_item = checkout_session.get('line_items')['data'][0]  # Get the first line item
                one_time_product_name = line_item.get('description')
                one_time_product_id = line_item.get('price').get('product')
                price_amount = line_item.get('amount_total') / 100.0  # Convert cents to dollars/euros
                currency = line_item.get('currency').upper()

                # Save the one-time purchase
                one_time_purchase = OneTimePurchase(
                    stripe_customer=stripe_customer,
                    product_name=one_time_product_name,
                    product_id=one_time_product_id,
                    price_amount=price_amount,
                    currency=currency,
                    status='completed',
                )
                one_time_purchase.save()
                print(f"One-time purchase saved for {user.username}.")


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