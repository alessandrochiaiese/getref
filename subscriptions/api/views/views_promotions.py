
from django.http import JsonResponse
from subscriptions.models.promotion import Promotion


def create_promotion(request):
    stripe_product_id = request.GET.get('stripeProductId')
    user = request.user  # Assumendo che l'utente sia autenticato

    # Verifica che esista un prodotto Stripe
    if not stripe_product_id:
        return JsonResponse({"error": "Stripe Product ID non valido."}, status=400)

    # Crea una promozione
    promotion = Promotion.objects.create(stripe_product_id=stripe_product_id, user=user)

    # Restituisce il link promozionale
    return JsonResponse({
        'promotionLink': str(promotion.promotion_link)
    })