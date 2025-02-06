from getref.settings import DOMAIN
import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User  # new
from django.http.response import JsonResponse, HttpResponse  # updated
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from subscriptions.models import StripeCustomer  # new


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

# Function to list Stripe products and their prices
def list_stripe_products():
    try:
        # Retrieve the products from Stripe
        products = stripe.Product.list()

        product_list = []

        for product in products.auto_paging_iter():
            # Retrieve prices associated with this product
            prices = stripe.Price.list(product=product.id)

            # Append the product and its prices to the list
            for price in prices.auto_paging_iter():
                product_list.append({
                    'product_name': product.name,
                    'product_id': product.id,
                    'price_id': price.id,
                    'price_amount': price.unit_amount,
                    'currency': price.currency,
                    'billing_scheme': price.billing_scheme
                })
        
        return product_list
    except stripe.error.StripeError as e:
        return {'error': f"Stripe Error: {str(e)}"}
    except Exception as e:
        return {'error': str(e)}

# The main function to create a checkout session
@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = DOMAIN
        stripe.api_key = settings.STRIPE_SECRET_KEY
        
        try:
            # Get the list of products and prices
            products = list_stripe_products()

            if not products:
                return JsonResponse({'error': 'No products found in Stripe.'}, status=404)

            # Select the first product's price_id (this could be dynamic based on your needs)
            selected_price_id = products[0]['price_id']

            # Create a checkout session with the selected price_id
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancel/',
                payment_method_types=['card'],
                mode='subscription',
                line_items=[{
                    'price': selected_price_id,  # Use the dynamic price_id
                    'quantity': 1,
                }]
            )

            # Return the session ID in the response
            return JsonResponse({'sessionId': checkout_session.id})

        except stripe.error.StripeError as e:
            return JsonResponse({'error': f"Stripe Error: {str(e)}"}, status=500)
        except Exception as e:
            return JsonResponse({'error': str(e)})
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
            stripe_customer_id=stripe_customer_id,
            stripe_subscription_id=stripe_subscription_id,
        )
        print(user.username + ' just subscribed.')

    return HttpResponse(status=200)
