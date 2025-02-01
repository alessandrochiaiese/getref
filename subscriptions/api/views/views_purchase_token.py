from getref.settings import DOMAIN
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.conf import settings
from subscriptions.models import *

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

"""
class PurchaseTokensAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        tokens_to_buy = request.data.get('tokens')
        price_entry = TokenPrice.objects.filter(quantity=tokens_to_buy).first()

        if not price_entry:
            return Response({"error": "Quantità di token non valida"}, status=400)

        # Aggiorna i token disponibili
        subscription, created = Subscription.objects.get_or_create(user=request.user)
        subscription.tokens_available += tokens_to_buy
        subscription.save()

        return Response({
            "message": f"Aggiunti {tokens_to_buy} token al tuo account.",
            "tokens_available": subscription.tokens_available,
        })
"""

class PurchaseTokensAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        package_id = request.data.get('package_id')  # L'ID del pacchetto scelto dall'utente
        user = request.user
        package = get_object_or_404(TokenPackage, id=package_id)

        try:
            # Crea una sessione di pagamento Stripe
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'eur',
                        'product_data': {
                            'name': f'Acquisto {package.name} ({package.tokens} token)',
                        },
                        'unit_amount': package.price_in_cents,  # Prezzo del pacchetto in centesimi
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=f'{DOMAIN}/success/',  # URL di successo
                cancel_url=f'{DOMAIN}/cancel/',  # URL di cancellazione
                client_reference_id=user.id,  # Passiamo l'ID dell'utente
                metadata={'package_id': package.id},
            )

            return Response({
                "session_id": checkout_session.id
            })

        except stripe.error.StripeError as e:
            return Response({"error": str(e)}, status=400)
