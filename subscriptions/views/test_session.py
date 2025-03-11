
from decimal import Decimal

from getref.settings import DOMAIN
from subscriptions.models.promotion import Promotion
from subscriptions.views.views_subscription import get_product_by_price_id, get_product_by_product_id
import stripe

def create_checkout_session(request, promotion_link=None, price_id=None, user_bonus=None, products=None):
    metadata = {}

    # Verifica se è presente un promotion_link
    if promotion_link:
        metadata = {
            'promotion_link': str(promotion_link)
        }
        try:
            # Recupera il venditore a partire dal promotion_link
            promotion = Promotion.objects.get(promotion_link=promotion_link)
            seller_stripe_account_id = promotion.seller.stripe_account_id  # L'ID dell'account Stripe del venditore
            selected_product = get_product_by_product_id(products, promotion.stripe_product_id)
        except Promotion.DoesNotExist:
            print("Promotion not found")
            selected_product = None
    elif price_id:
        selected_product = get_product_by_price_id(products, price_id)
    
    # Calcola l'importo totale
    product_price = Decimal(selected_product['price'])  # Assicurati che il prezzo sia un valore decimale
    if user_bonus:
        discount_amount = product_price * Decimal(0.05)  # 5% di sconto per l'utente
        discounted_price = product_price - discount_amount
    else:
        discounted_price = product_price

    # Crea una sessione di checkout
    checkout_session = stripe.checkout.Session.create(
        client_reference_id=request.user.id if request.user.is_authenticated else None,
        success_url=f"{DOMAIN}/success?session_id={{CHECKOUT_SESSION_ID}}",
        cancel_url=f"{DOMAIN}/cancel/",
        payment_method_types=['card'],
        mode='payment',  # Modalità di pagamento
        line_items=[{
            'price_data': {
                'currency': 'usd',  # Modifica la valuta secondo le tue necessità
                'product_data': {
                    'name': selected_product['name'],
                },
                'unit_amount': int(discounted_price * 100),  # L'importo deve essere in centesimi
            },
            'quantity': 1,
        }],
        metadata=metadata,
        customer_email=request.user.email if request.user.is_authenticated else None,
        # Aggiungi lo sconto del 5% se presente
        discounts=[{
            'coupon': '5_percent_off'  # Id del coupon di Stripe per il 5% di sconto
        }] if user_bonus else [],
        payment_intent_data={
            'application_fee_amount': int(product_price * Decimal(0.15) * 100),  # 15% della transazione va al venditore
            'transfer_data': {
                'destination': seller_stripe_account_id  # Account Stripe del venditore
            }
        },
        customer_creation='always',  # Forza la creazione del cliente se non esiste
    )

    return checkout_session

"""
# Funzione per recuperare il prodotto dalla lista in base all'ID prodotto
def get_product_by_product_id(products, product_id):
    return next((product for product in products if product['id'] == product_id), None)

# Esegui la funzione passando i parametri richiesti
checkout_session = create_checkout_session(request, promotion_link='c889609f-6f27-4da4-b977-52eb2476f574', user_bonus=True, price_id='price_1234', products=some_product_list)

print("Checkout session created:", checkout_session.url)
"""