#DOMAIN='https://affiliate.getcall.it'
from getref.settings import DOMAIN
import stripe
from getref import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.response import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from subscriptions.models import StripeCustomer 

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
                mode='payment',
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
        stripe_customer = StripeCustomer.objects.get(user=request.user)
        # load stipe secret key here
        subscriptions = stripe.Subscription.list(customer=stripe_customer.stripeCustomerId)

        return render(request, 'subscriptions/pages.html', {
            'subscriptions': subscriptions,
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
    # load stipe secret key here
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
