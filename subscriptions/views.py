#DOMAIN='https://affiliate.getcall.it'
from getref.settings import DOMAIN
import stripe
from getref import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from subscriptions.models import StripeCustomer, StripeSubscription 

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
        products = list_stripe_products()

        return render(request, 'subscriptions/plans.html', {
            'subscription': subscription,
            'product': product,
            'products': products,  # Pass the list of products to the template
        })

    except StripeCustomer.DoesNotExist:
        # If the user doesn't have an active subscription
        products = list_stripe_products()
        return render(request, 'subscriptions/plans.html', {
            'products': products,
        })


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

# Funzione per recuperare i prodotti e i prezzi da Stripe
def list_stripe_products():
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
                    'billing_scheme': price.billing_scheme
                })
        
        print(f"Prodotti recuperati: {product_list}")  # Log per vedere i prodotti recuperati
        return product_list
    except stripe.error.StripeError as e:
        print(f"Errore Stripe: {str(e)}")  # Log di errore Stripe
        return {'error': f"Stripe Error: {str(e)}"}
    except Exception as e:
        print(f"Errore generico: {str(e)}")  # Log di errore generico
        return {'error': str(e)}

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        # load stipe secret key here
        price_id = request.GET.get('priceId')

        try:
            if not price_id:
                return JsonResponse({'error': 'No price ID found.'}, status=400)

            # Create checkout session
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=f"{DOMAIN}/success?session_id={{CHECKOUT_SESSION_ID}}",
                cancel_url=f"{DOMAIN}/cancel/",
                payment_method_types=['card'],
                mode='subscription',
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
        #stripe_customer = StripeCustomer.objects.get(user=request.user)
        #subscriptions = stripe_customer.subscriptions.all()  # Recupera tutti gli abbonamenti dell'utente

        """purchased_products = []
        for subscription in subscriptions:
            purchased_products.append({
                'product_name': subscription.product_name,
                'product_id': subscription.product_id,
                'status': subscription.status,
                'subscription_date': subscription.subscription_date,
            })

        return render(request, 'subscriptions/pages.html', {
            'purchased_products': purchased_products,
        })"""

        # Recupera tutte le sottoscrizioni per questo cliente
        subscriptions = StripeSubscription.objects.filter(stripe_customer__user=request.user)

        # Passa i dati al template
        return render(request, 'subscriptions/pages.html', {
            'subscriptions': subscriptions,  # Passa le sottoscrizioni al template
        })
    except StripeCustomer.DoesNotExist:
        return render(request, 'subscriptions/pages.html', {
            'subscriptions': [],
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
        stripe_subscription_id = checkout_session.get('subscription')  # Questo può essere null se il checkout non è per una sottoscrizione

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
            stripe_customer = StripeCustomer(
                user=user,
                stripeCustomerId=stripe_customer_id,
                stripeSubscriptionId=stripe_subscription_id,
            )
            stripe_customer.save()

            if stripe_customer:
                print(f"StripeCustomer for user {user.username} created.")
            else:
                print(f"StripeCustomer for user {user.username} already exists.")

            # Recupere la subscription
            stripe_subscription = stripe.Subscription.retrieve(stripe_subscription_id)
            
            # Log della subscription
            print(f"Subscription details: {subscription}")
            
            # Salva la subscription (modifica come necessario)
            subscription = StripeSubscription(
                stripe_customer=stripe_customer,
                stripe_subscription_id=stripe_subscription_id,
                product_name=stripe_subscription.plan.product.name,
                product_id=stripe_subscription.plan.product.id,
                status=stripe_subscription.status,
            )
            print(f"Subscription saved for {user.username}.")
            subscription.save()

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