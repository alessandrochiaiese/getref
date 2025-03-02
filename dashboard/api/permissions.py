from dashboard.models.profile import Profile
from rest_framework.permissions import BasePermission
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

class HasActiveSubscription(BasePermission):
    def has_permission(self, request, view):
        # Se l'utente è un amministratore o una piattaforma (verificato tramite Profile), permetti l'accesso
        profile = Profile.objects.filter(user=request.user)
        if request.user.is_staff or getattr(request.user.profile, 'is_platform', False) or profile.is_platform:
            return True

        # Verifica l'abbonamento per gli utenti normali
        user_id = request.user.id
        subscriptions = stripe.Subscription.list(customer=user_id)

        for subscription in subscriptions:
            if subscription.status == 'active':
                return True
        return False
