from getref.settings import DOMAIN
import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User  # new
from django.http.response import JsonResponse, HttpResponse  # updated
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from subscriptions.models import StripeCustomer  # new

"""
@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = DOMAIN
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancel/',
                payment_method_types=['card'],
                mode='subscription',
                line_items=[
                    {
                        'price': settings.STRIPE_PRICE_ID,
                        'quantity': 1,
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session.id})
        except stripe.error.StripeError as e:
            # Gestisci errori specifici di Stripe
            return JsonResponse({'error': f"Stripe Error: {str(e)}"}, status=500)
        except Exception as e:
            return JsonResponse({'error': str(e)})
"""

@login_required
def home(request):
    try:
        # Retrieve the subscription & product
        stripe_customer = StripeCustomer.objects.get(user=request.user)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        subscription = stripe.Subscription.retrieve(stripe_customer.stripeSubscriptionId)
        product = stripe.Product.retrieve(subscription.plan.product)

        # Feel free to fetch any additional data from 'subscription' or 'product'
        # https://stripe.com/docs/api/subscriptions/object
        # https://stripe.com/docs/api/products/object

        return render(request, 'home.html', {
            'subscription': subscription,
            'product': product,
        })

    except StripeCustomer.DoesNotExist:
        return render(request, 'subscriptions/home.html')


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
                    'price_amount': price.unit_amount,
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
        stripe.api_key = settings.STRIPE_SECRET_KEY
        
        try:
            print("Recupero dei prodotti e dei prezzi...")  # Log for debugging
            products = list_stripe_products()

            if not products:
                print("Nessun prodotto trovato in Stripe.")  # Log if no products found
                return JsonResponse({'error': 'No products found in Stripe.'}, status=404)

            # Select the first product and its price_id
            selected_price_id = products[0]['price_id']  # or 'price_1PP6aqLA6EOGRbboQRdBlx27'

            if not selected_price_id:
                print("Nessun price_id trovato per il prodotto selezionato.")  # Log if no price_id
                return JsonResponse({'error': 'No price ID found for selected product.'}, status=404)

            print(f"Price ID selezionato: {selected_price_id}")  # Log selected price_id

            # Create checkout session
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=DOMAIN + '/success?session_id={CHECKOUT_SESSION_ID}',  # Corrected URL
                cancel_url=DOMAIN + '/cancel/',
                payment_method_types=['card'],
                mode='subscription',  # Use 'payment' if it's a one-time payment
                line_items=[{
                    'price': selected_price_id,  # Use dynamic price_id
                    'quantity': 1,
                }]
            )
            print(f"Success URL: {DOMAIN + '/success?session_id={CHECKOUT_SESSION_ID}'}")
            print(f"Cancel URL: {DOMAIN + '/cancel/'}")
            print("Sessione di checkout:", checkout_session)  # Log the checkout session

            if not checkout_session or 'id' not in checkout_session:
                print("Errore: la sessione di checkout non è stata creata correttamente.")  # Log if session creation fails
                return JsonResponse({'error': 'Failed to create checkout session.'}, status=500)

            print(f"Sessione di checkout creata con successo. Session ID: {checkout_session.id}")  # Log success

            # Return the sessionId as a response
            return JsonResponse({'sessionId': checkout_session.id})

        except stripe.error.StripeError as e:
            print(f"Errore Stripe: {str(e)}")  # Log Stripe errors
            return JsonResponse({'error': f"Stripe Error: {str(e)}"}, status=500)
        except Exception as e:
            print(f"Errore generale: {str(e)}")  # Log general errors
            return JsonResponse({'error': str(e)})



@login_required
def success(request):
    return render(request, 'subscriptions/success.html')


@login_required
def cancel(request):
    return render(request, 'subscriptions/cancel.html')


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        # Fetch all the required data from session
        client_reference_id = session.get('client_reference_id')
        stripe_customer_id = session.get('customer')
        stripe_subscription_id = session.get('subscription')

        # Get the user and create a new StripeCustomer
        user = User.objects.get(id=client_reference_id)
        StripeCustomer.objects.create(
            user=user,
            stripeCustomerId=stripe_customer_id,
            stripeSubscriptionId=stripe_subscription_id,
        )
        print(user.username + ' just subscribed.')

    return HttpResponse(status=200)
