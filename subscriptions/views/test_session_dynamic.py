
from decimal import Decimal

from getref.settings import DOMAIN
from subscriptions.models.promotion import Promotion
from subscriptions.views.views_subscription import get_product_by_price_id, get_product_by_product_id
import stripe
import stripe
from decimal import Decimal

stripe.api_key = 'your_stripe_secret_key'

def create_checkout_session(request, promotion_link=None, price_id=None, user_bonus=None, products=None):
    metadata = {}

    # Verifica se c'è un link promozionale
    if promotion_link:
        # Ottieni i dettagli del venditore e del prodotto promozionale
        metadata = {
            'promotion_link': str(promotion_link)
        }
        try:
            promotion = Promotion.objects.get(promotion_link=promotion_link)
            seller_stripe_account_id = promotion.seller.stripe_account_id  # Account Stripe del venditore
            selected_product = get_product_by_product_id(products, promotion.stripe_product_id)
        except Promotion.DoesNotExist:
            print("Promotion not found")
            selected_product = None
    elif price_id:
        # Se non c'è un link promozionale, seleziona il prodotto normale
        selected_product = get_product_by_price_id(products, price_id)
    
    # Verifica se il prodotto è valido
    if not selected_product:
        return {"error": "Product not found"}

    # Calcola il prezzo del prodotto e lo sconto per l'utente (se presente)
    product_price = Decimal(selected_product['price'])  # Prezzo del prodotto
    if user_bonus:
        discount_amount = product_price * Decimal(0.05)  # 5% di sconto per l'utente
        discounted_price = product_price - discount_amount
    else:
        discounted_price = product_price

    # Crea la sessione di checkout con parametri dinamici
    checkout_params = {
        'client_reference_id': request.user.id if request.user.is_authenticated else None,
        'success_url': f"{DOMAIN}/success?session_id={{CHECKOUT_SESSION_ID}}",
        'cancel_url': f"{DOMAIN}/cancel/",
        'payment_method_types': ['card'],
        'mode': 'payment',  # Modalità di pagamento
        'line_items': [{
            'price_data': {
                'currency': 'usd',  # Modifica la valuta
                'product_data': {
                    'name': selected_product['name'],
                },
                'unit_amount': int(discounted_price * 100),  # L'importo deve essere in centesimi
            },
            'quantity': 1,
        }],
        'metadata': metadata,  # Aggiungi metadata promozionale, se presente
        'customer_email': request.user.email if request.user.is_authenticated else None,
        'customer_creation': 'always',  # Forza la creazione del cliente se non esiste
    }

    # Se il link promozionale è presente, aggiungi commissioni al venditore
    if promotion_link:
        checkout_params['payment_intent_data'] = {
            'application_fee_amount': int(product_price * Decimal(0.15) * 100),  # 15% di commissione
            'transfer_data': {
                'destination': seller_stripe_account_id  # Destinazione dell'importo al venditore
            }
        }
    
    # Se c'è uno sconto per l'utente, applicalo alla sessione
    if user_bonus:
        checkout_params['discounts'] = [{
            'coupon': '5_percent_off'  # Supponendo tu abbia creato un coupon in Stripe con id '5_percent_off'
        }]
    
    # Creazione della sessione di checkout
    try:
        checkout_session = stripe.checkout.Session.create(**checkout_params)
        return checkout_session
    except stripe.error.StripeError as e:
        return {"error": str(e)}

# Funzione per recuperare il prodotto dal database (esempio)
def get_product_by_product_id(products, product_id):
    return next((product for product in products if product['id'] == product_id), None)

def get_product_by_price_id(products, price_id):
    return next((product for product in products if product['price_id'] == price_id), None)
"""
# Esegui la creazione della sessione di checkout
checkout_session = create_checkout_session(
    request, 
    promotion_link='c889609f-6f27-4da4-b977-52eb2476f574', 
    user_bonus=True, 
    price_id='price_1234', 
    products=some_product_list
)

# Restituisci l'URL per la sessione di checkout
if 'error' in checkout_session:
    print("Error:", checkout_session['error'])
else:
    print("Checkout session created. Visit:", checkout_session.url)
"""