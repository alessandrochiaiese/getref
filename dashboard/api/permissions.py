import datetime
from dashboard.models.profile import Profile
from rest_framework.permissions import BasePermission
from django.conf import settings
import stripe
from subscriptions.models.api_key import APIKey
from subscriptions.models.stripe_customer import StripeCustomer

stripe.api_key = settings.STRIPE_SECRET_KEY


DAY_PER_MONTH = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

PLANS = {
    "subscriptions": [
        {
            "id": "affiliate-basic",
            "name": "Affiliate System - Base",
            "features": "Dashboard affiliato: ✔, Monitoraggio commissioni: ✔, Pagamenti mensili: ✔, Integrazione API: ❌, Tracciamento in tempo reale: ❌, Supporto: Email",

        },
        {
            "id": "affiliate-pro",
            "name": "Affiliate System - Pro",
            "features": "Dashboard affiliato: ✔, Monitoraggio commissioni: ✔, Pagamenti settimanali: ✔, Integrazione API: ✔, Tracciamento in tempo reale: ✔, Supporto: Email e Chat",

        },
        {
            "id": "affiliate-premium",
            "name": "Affiliate System - Premium",
            "features": "Dashboard affiliato: ✔, Monitoraggio commissioni: ✔, Pagamenti giornalieri: ✔, Integrazione API: ✔, Tracciamento in tempo reale: ✔, Strumenti di marketing: ✔, Supporto: Email, Chat e Telefono",

        },    
        {
            "id": "referral-basic",
            "name": "Referral Code System - Base",
            "features": "Generazione codici referral: ✔, Tracciamento conversioni: ✔, Gestione ricompense: ✔, Reportistica avanzata: ❌, Personalizzazione ricompense: ❌, Supporto: Email",

        },
        {
            "id": "referral-pro",
            "name": "Referral Code System - Pro",
            "features": "Generazione codici referral: ✔, Tracciamento conversioni: ✔, Gestione ricompense: ✔, Reportistica avanzata: ✔, Personalizzazione ricompense: ✔, Supporto: Email e Chat",

        },
        {
            "id": "referral-premium",
            "name": "Referral Code System - Premium",
            "features": "Generazione codici referral: ✔, Tracciamento conversioni: ✔, Gestione ricompense: ✔, Reportistica avanzata: ✔, Personalizzazione ricompense: ✔, Campagne personalizzate: ✔, Analisi avanzate: ✔, Supporto: Email, Chat e Telefono",
                    
        }
    ]
}

class HasActiveSubscription(BasePermission):
    def has_permission(self, request, view):
        # Se l'utente è un amministratore o una piattaforma, permetti l'accesso
        profile = Profile.objects.filter(user=request.user).first()  # Otteniamo il profilo dell'utente
        if request.user.is_staff or getattr(request.user.profile, 'is_platform', False) or profile.is_platform:
            return True

        # Recupera il cliente Stripe
        stripe_customer = StripeCustomer.objects.get(user=request.user)

        # Recupera tutte le sottoscrizioni attive
        subscriptions = stripe.Subscription.list(customer=stripe_customer.stripeCustomerId, status='active')

        # Ottieni la classe della view che ha chiamato questa permission
        api_view_class = view.__class__

        # Trova una sottoscrizione attiva con piano mensile
        active_subscription = None
        plan_type = None
        for subscription in subscriptions['data']:
            product = stripe.Product.retrieve(subscription['plan']['product'])
            plan_type = self.check_api_services(api_view_class, product)
            if subscription.status == 'active' and subscription.items.data[0].plan.interval == 'month':
                active_subscription = subscription
                break  # Puoi interrompere il loop se trovi una sottoscrizione valida

        if active_subscription and plan_type is not None:
            # Verifica che l'utente sviluppatore abbia effettivamente creato almeno una API
            if self.has_created_apis(request.user):
                api_key = APIKey.objects.filter(user=request.user, is_active=True).first()
                api_key.request_count += 1
                api_key.save()
                # Ottieni la data corrente
                current_date = datetime.datetime.now()
                current_year = current_date.year
                current_month = current_date.month
                current_day = current_date.day 
                 
                # Verifica se il mese di sottoscrizione è diverso dal mese corrente
                if api_key:
                    # Ottieni la data di sottoscrizione (dovresti avere un campo che memorizza la data di creazione o di ultimo reset)
                    subscription_date = api_key.created_at
                    subscription_month = subscription_date.month
                    subscription_year = subscription_date.year
                    subscription_day = subscription_date.day

                    # Se è il primo giorno del mese o se il mese è cambiato, azzera il contatore
                    if current_month != subscription_month or current_year != subscription_year:
                        # Azzerare il request_count
                        api_key.request_count = 0
                        
                        # Aggiorna la data di sottoscrizione al nuovo mese
                        api_key.created_at = current_date
                        
                        # Salva la modifica
                        api_key.save()

                    # Aumenta il contatore delle richieste per il mese corrente
                    api_key.request_count += 1
                    api_key.save()
                return True
            else:
                return False
        else:
            return False

    def check_api_services(self, api_view_class, product):
        affiliate_basic = "Dashboard affiliato: ✔, Monitoraggio commissioni: ✔, Pagamenti mensili: ✔, Integrazione API: ❌, Tracciamento in tempo reale: ❌, Supporto: Email"
        affiliate_pro = "Dashboard affiliato: ✔, Monitoraggio commissioni: ✔, Pagamenti settimanali: ✔, Integrazione API: ✔, Tracciamento in tempo reale: ✔, Supporto: Email e Chat"
        affiliate_premium = "Dashboard affiliato: ✔, Monitoraggio commissioni: ✔, Pagamenti giornalieri: ✔, Integrazione API: ✔, Tracciamento in tempo reale: ✔, Strumenti di marketing: ✔, Supporto: Email, Chat e Telefono"
        referral_basic = "Generazione codici referral: ✔, Tracciamento conversioni: ✔, Gestione ricompense: ✔, Reportistica avanzata: ❌, Personalizzazione ricompense: ❌, Supporto: Email"
        referral_pro = "Generazione codici referral: ✔, Tracciamento conversioni: ✔, Gestione ricompense: ✔, Reportistica avanzata: ✔, Personalizzazione ricompense: ✔, Supporto: Email e Chat"
        referral_premium = "Generazione codici referral: ✔, Tracciamento conversioni: ✔, Gestione ricompense: ✔, Reportistica avanzata: ✔, Personalizzazione ricompense: ✔, Campagne personalizzate: ✔, Analisi avanzate: ✔, Supporto: Email, Chat e Telefono"
        match api_view_class:
            case 'AffiliateAuditAPIView':
                if affiliate_basic in product['metadata']['features']:
                    return product['name']
            case 'AffiliateCampaignAPIView':
                if affiliate_premium in product['metadata']['features']:
                    return product['name']
            case 'AffiliateCommissionAPIView':
                if affiliate_pro in product['metadata']['features']:
                    return product['name']
            case 'AffiliateLinkAPIView':
                if affiliate_basic in product['metadata']['features']:
                    return product['name']
            case 'AffiliateNotificationAPIView':
                if affiliate_pro in product['metadata']['features']:
                    return product['name']
            case 'AffiliatePayoutAPIView':
                if affiliate_premium in product['metadata']['features']:
                    return product['name']
            case 'AffiliatePerformanceAPIView':
                if affiliate_pro in product['metadata']['features']:
                    return product['name']
            case 'AffiliateProgramPartecipationAPIView':
                if affiliate_premium in product['metadata']['features']:
                    return product['name']
            case 'AffiliateProgramAPIView':
                if affiliate_premium in product['metadata']['features']:
                    return product['name']
            case 'AffiliateRewardAPIView':
                if affiliate_basic in product['metadata']['features']:
                    return product['name']
            case 'AffiliateSettingsAPIView':
                if affiliate_basic in product['metadata']['features']:
                    return product['name']
            case 'AffiliateSupportTicketAPIView':
                if affiliate_premium in product['metadata']['features']:
                    return product['name']
            case 'AffiliateTierAPIView':
                if affiliate_premium in product['metadata']['features']:
                    return product['name']
            case 'AffiliateTransactionAPIView':
                if affiliate_premium in product['metadata']['features']:
                    return product['name']
            case 'ReferralAuditAPIView':
                if referral_basic in product['metadata']['features']:
                    return product['name']
            case 'ReferralBonusAPIView':
                if referral_premium in product['metadata']['features']:
                    return product['name']
            case 'ReferralCampaignAPIView':
                if referral_premium in product['metadata']['features']:
                    return product['name']
            case 'ReferralCodeAPIView':
                if referral_basic in product['metadata']['features']:
                    return product['name']
            case 'ReferralConversionAPIView':
                if referral_pro in product['metadata']['features']:
                    return product['name']
            case 'ReferralNotificationAPIView':
                if referral_pro in product['metadata']['features']:
                    return product['name']
            case 'ReferralProgramPatecipationAPIView':
                if referral_premium in product['metadata']['features']:
                    return product['name']
            case 'ReferralProgramAPIView':
                if referral_premium in product['metadata']['features']:
                    return product['name']
            case 'ReferralRewardAPIView':
                if referral_pro in product['metadata']['features']:
                    return product['name']
            case 'ReferralSettingsAPIView':
                if referral_pro in product['metadata']['features']:
                    return product['name']
            case 'ReferralStatsAPIView':
                if referral_pro in product['metadata']['features']:
                    return product['name']
            case 'ReferralTransactionAPIView':
                if referral_pro in product['metadata']['features']:
                    return product['name']
        return None
    
    def check_api_services_dopo_modifiche_ai_prodotti_stripe(self, api_view_class, product):
        """
        Verifica se il piano della sottoscrizione dà accesso alla classe API specificata
        """
        # Supponiamo che tu abbia un campo `metadata` con l'accesso alle API
        if 'access' in product.metadata:
            accessible_views = product.metadata['access']
            if str(api_view_class) in accessible_views:
                return True
        return False

    def has_created_apis(self, user):
        # Verifica che l'utente abbia almeno una API key attiva
        api_key = APIKey.objects.filter(user=user, is_active=True).first()

        # Se non esiste una chiave attiva, crea una nuova chiave API per l'utente
        if not api_key:
            APIKey.create_api_key(user)
            return True
        
        return api_key is not None
    
    def has_created_api_simple(self, user):
        # Verifica che l'utente abbia almeno una API key attiva
        return APIKey.objects.filter(user=user, is_active=True).exists()
    
    def has_created_apisfdsfds(self, user):
        """
        Verifica se l'utente ha creato almeno una API.
        Supponiamo che tu abbia un modello `API` che rappresenta le API create dagli sviluppatori
        """
        # Verifica se l'utente ha creato almeno una API
        created_apis = APIKey.objects.filter(creator=user)  # Assuming you have a `creator` field linking to the user
        return created_apis.exists()  # Return True if there are APIs created by the user
    

"""  
class HasActiveSubscription(BasePermission):
    def has_permission(self, request, view):
        # Se l'utente è un amministratore o una piattaforma, permetti l'accesso
        profile = Profile.objects.filter(user=request.user).first()  # Otteniamo il profilo dell'utente
        if request.user.is_staff or getattr(request.user.profile, 'is_platform', False) or profile.is_platform:
            return True

        # Recupera il cliente Stripe
        stripe_customer = StripeCustomer.objects.get(user=request.user)

        # Recupera tutte le sottoscrizioni attive
        subscriptions = stripe.Subscription.list(customer=stripe_customer.stripeCustomerId, status='active')

        # Ottieni la classe della view che ha chiamato questa permission
        api_view_class = view.__class__

        # Trova una sottoscrizione attiva con piano mensile
        active_subscription = None
        for subscription in subscriptions:
            if subscription.status == 'active' and subscription.items.data[0].plan.interval == 'month':
                active_subscription = subscription
                # Supponiamo che la sottoscrizione abbia un 'metadata' che contiene i permessi per le API
                # Ad esempio: 'subscription.plan.metadata['access']' contiene una lista di classi autorizzate
                if 'access' in subscription.items.data[0].plan.metadata:
                    accessible_views = subscription.items.data[0].plan.metadata['access']
                    # Verifica se la classe della view è presente tra le classi autorizzate
                    if str(api_view_class) in accessible_views:
                        return True
                break  # Puoi interrompere il loop se trovi una sottoscrizione valida

        # Se non viene trovata una sottoscrizione attiva con accesso, ritorna False
        return False
#metadata={
#    'access': ['YourAPIViewClassName', 'AnotherAPIViewClassName']
#}

class HasActiveSubscription(BasePermission):
    def has_permission(self, request, view):
        # Se l'utente è un amministratore o una piattaforma, permetti l'accesso
        profile = Profile.objects.filter(user=request.user).first()  # Otteniamo il profilo dell'utente
        if request.user.is_staff or getattr(request.user.profile, 'is_platform', False) or profile.is_platform:
            return True

        # Verifica che l'utente abbia un abbonamento attivo e che il piano sia mensile
        #user_id = request.user.id
        stripe_customer = StripeCustomer.objects.get(user=request.user)

        subscriptions = stripe.Subscription.list(customer=stripe_customer.stripeCustomerId, status='active')

        # Trova l'abbonamento attivo con pagamento mensile
        active_subscription = None
        for subscription in subscriptions:
            if subscription.status == 'active' and subscription.items.data[0].plan.interval == 'month':
                active_subscription = subscription
                break

        if active_subscription:
            return True
        else:
            return False
      
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
"""