
import logging
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View 
from django.views.generic import TemplateView
from dashboard.models import * 
from referral.models import * 
from dashboard.forms import * 
from dashboard.utils import calculate_user_level, get_tree_referred, tree_to_list

User = get_user_model()

@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    model = get_user_model()  # Usa il modello User di default
    template_name = 'dashboard/index.html'

    def get_object(self, queryset=None):
        # Ritorna l'oggetto corrispondente all'utente autenticato
        return self.request.user
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the user 
        user=self.request.user#user = User.objects.filter(user=self.request.user).first()

        # Get the user's profile
        profile = Profile.objects.filter(user=user).first()

        # Get the referral code for the user
        referral_code = ReferralCode.objects.filter(user=user).first()
 
        # Get the user's referral information
        try:
            referral = Referral.objects.filter(referrer=user).first()
        except Exception:
            referrer = None

        referrer = None
        referrer_code = None
        # Get the referral code for the referrer
        try:
            referrer = ReferralCode.objects.filter(user=referral.referrer).first()
        except Exception:
            referrer = None

        # If the referrer exists, get the referrer code
        if referrer:
            referrer_code = referrer.code
        else:
            referrer_code = None
 
        # Add the referral code to the context
        try: 
            context['referral_code'] = referral_code.code
            context['referral_unique_url'] = referral_code.unique_url
        except AttributeError:
            context['referral_code'] = None
            context['referral_unique_url'] = None
        
        # Add the referrer code to the context
        try: 
            context['referrer_code'] = referrer_code
        except AttributeError:
            context['referrer_code'] = None
 
        # Retrieve all referrals made by the logged-in user
        referred_users = []

        referral = None
        try:
            # Recupera tutti i Referral dell'utente autenticato
            referral = Referral.objects.filter(referrer=user).first() 
            print(referral)
            
        except Exception:
            referrer = None
        
        if referral != None:
            # Itera sui Referral e aggiungi gli utenti collegati alla lista
            for referred in referral.referred.all():
                referred_users.append(referred)  # Usa .all() per ottenere gli oggetti collegati

            # Debug: Stampa gli utenti invitati
            print("Final referred users list:", referred_users)
            # Debug: Print the final list of referred users
            print("Final Referred Users:", referred_users)

            # Pass the referred users to the context
            context['referred_users'] = referred_users

        referreds = []
        tree_referred = get_tree_referred(user, level=0)
        list_referred = tree_to_list(tree_referred, referreds)
        
        print(tree_referred)
        print(list_referred)
        context['referred_leveled_users'] = list_referred
        
        return context
    
@method_decorator(login_required, name='dispatch')
class MasterAccountsView(TemplateView):
    model = get_user_model()  # Usa il modello User di default
    template_name = 'dashboard/referred_accounts/master_accounts.html'

    def get_object(self, queryset=None):
        # Ritorna l'oggetto corrispondente all'utente autenticato
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the user
        user = self.request.user

        # Get the user's profile
        profile = Profile.objects.filter(user=user).first()

        # Get the referral code for the user
        referral_code = ReferralCode.objects.filter(user=user).first()

        # Get the referral where the user is referred
        referral = None
        try:
            referral = Referral.objects.filter(referred=user).first()
        except Exception as e:
            print(e)

        
        # Initialize referrer and referrer_code
        referrer = None
        referrer_code = None

        # Check if referral exists
        if referral:
            # If the user has been referred, get the referrer and their referral code
            referrer = referral.referrer  # This is the user who invited the current user
            referrer_code = ReferralCode.objects.filter(user=referrer).first()  # Get the referrer code

            # Debugging print to see the referrer and referred information
            print(f"Referrer: {referrer}, Referred: {referral.referred}")

        else:
            # If no referral is found, handle it gracefully
            print("No referral found for this user.")
 
        context['master_account'] = referrer
        
        return context
    

@method_decorator(login_required, name='dispatch')
class InvestorAccountsView(TemplateView):
    model = get_user_model()  # Usa il modello User di default
    template_name = 'dashboard/referred_accounts/investor_accounts.html'

    def get_object(self, queryset=None):
        # Ritorna l'oggetto corrispondente all'utente autenticato
        return self.request.user
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the user 
        user=self.request.user#user = User.objects.filter(user=self.request.user).first()

        # Get the user's profile
        profile = Profile.objects.filter(user=user).first()

        # Get the referral code for the user
        referral_code = ReferralCode.objects.filter(user=user).first()
 
        # Get the user's referral information
        try:
            referral = Referral.objects.filter(referrer=user).first()
        except Exception:
            referrer = None

        referrer = None
        referrer_code = None
        # Get the referral code for the referrer
        try:
            referrer = ReferralCode.objects.filter(user=referral.referrer).first()
        except Exception:
            referrer = None

        # If the referrer exists, get the referrer code
        if referrer:
            referrer_code = referrer.code
        else:
            referrer_code = None
 
        # Add the referral code to the context
        try: 
            context['referral_code'] = referral_code.code
        except AttributeError:
            context['referral_code'] = None
        
        # Add the referrer code to the context
        try: 
            context['referrer_code'] = referrer_code
        except AttributeError:
            context['referrer_code'] = None

        
        # Retrieve all referrals made by the logged-in user
        referred_users = []

        referral = None
        try:
            # Recupera tutti i Referral dell'utente autenticato
            referral = Referral.objects.filter(referrer=user).first() 
            print(referral)
            
        except Exception:
            referrer = None
        
        if referral != None:
            # Itera sui Referral e aggiungi gli utenti collegati alla lista
            for referred in referral.referred.all():
                referred_users.append(referred)  # Usa .all() per ottenere gli oggetti collegati

            # Debug: Stampa gli utenti invitati
            print("Final referred users list:", referred_users)
            # Debug: Print the final list of referred users
            print("Final Referred Users:", referred_users)

            # Pass the referred users to the context
            context['referred_users'] = referred_users

        referreds = []
        tree_referred = get_tree_referred(user, level=0)
        list_referred = tree_to_list(tree_referred, referreds)
        investor_accounts = []

        for referred_item in list_referred:
            print(f"Referred Item: {referred_item}")  # Aggiungi un log per verificare il contenuto
            
            referred_id = referred_item.get('id')
            if referred_id is None:
                print(f"Warning: referred_item has no 'id': {referred_item}")
                continue  # Vai al prossimo elemento
            
            referred_user = User.objects.filter(id=referred_id).first()
            if referred_user:
                print(f"Found user: {referred_user}")
                referred = Profile.objects.filter(user=referred_user).first()
                
                if referred:
                    print(f"Found profile for user: {referred.user}")
                    print(f"Is buyer for {referred.user}: {referred.is_buyer}")
                    
                    transactions = ReferralTransaction.objects.filter(referred_user=referred.user)
                    print(f"Transactions for {referred.user}: {transactions.count()}")
                    
                    if referred.is_buyer: #if transactions.exists() or referred.is_buyer:
                        investor_accounts.append(referred_item)
                else:
                    print(f"Profile not found for user: {referred_user}")
            else:
                print(f"User with ID {referred_id} not found.")

        print(investor_accounts)
        context['investor_accounts'] = investor_accounts
        
        return context
    

logger = logging.getLogger(__name__)
@method_decorator(login_required, name='dispatch')
class IncompleteRegistrationsView(TemplateView):
    template_name = 'dashboard/referred_accounts/incomplete_registrations.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_referral_code(self, user):
        try:
            return ReferralCode.objects.filter(user=user).first().code
        except AttributeError:
            return None

    def get_referred_users(self, user):
        # Otteniamo gli utenti inviati da un utente
        referral = Referral.objects.filter(referrer=user.id).first()
        return referral.referred.all() if referral else []

    def get_incomplete_registrations(self, user):
        incomplete_registrations = []
        # Otteniamo gli utenti inviati
        referred_users = self.get_referred_users(user)
        
        for referred_user in referred_users:
            # Verifica se il profilo dell'utente inviato è incompleto
            profile = Profile.objects.filter(user=referred_user).first()
            if profile:
                # Controlla se ci sono attributi del profilo mancanti
                if not all([profile.birth_date, profile.city, profile.street, profile.CAP, profile.phone_number]):
                    incomplete_registrations.append(referred_user)

        return incomplete_registrations

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        referral_code = self.get_referral_code(user)
        referrer_code = None

        try:
            # Recupera il codice del referrer (se esiste)
            referral = Referral.objects.filter(referrer=user).first()
            if referral:
                referrer = ReferralCode.objects.filter(user=referral.referrer.id).first()
                if referrer:
                    referrer_code = referrer.code
        except Exception as e:
            logger.error(f"Error occurred: {e}")

        # Ottieni gli utenti inviati incompleti
        incomplete_referred_users = self.get_incomplete_registrations(user)

        context['referral_code'] = referral_code
        context['referrer_code'] = referrer_code
        print("X ", incomplete_referred_users)
        context['incomplete_referred_users'] = [
            {
                'first_name': x.first_name,
                'last_name': x.last_name,
                'username': x.username,
                'level': calculate_user_level(x),
                'date_joined': x.date_joined
            } for x in incomplete_referred_users]
        print("X ", incomplete_referred_users)
        return context

    
@method_decorator(login_required, name='dispatch')
class MyNetworkView(TemplateView):
    model = get_user_model()  # Usa il modello User di default
    template_name = 'dashboard/referred_accounts/my_network.html'

    def get_object(self, queryset=None):
        # Ritorna l'oggetto corrispondente all'utente autenticato
        return self.request.user
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the user 
        user=self.request.user#user = User.objects.filter(user=self.request.user).first()

        # Get the user's profile
        profile = Profile.objects.filter(user=user).first()

        # Get the referral code for the user
        referral_code = ReferralCode.objects.filter(user=user).first()
 
        # Get the user's referral information
        try:
            referral = Referral.objects.filter(referrer=user).first()
        except Exception:
            referrer = None

        referrer = None
        referrer_code = None
        # Get the referral code for the referrer
        try:
            referrer = ReferralCode.objects.filter(user=referral.referrer.id).first()
        except Exception:
            referrer = None

        # If the referrer exists, get the referrer code
        if referrer:
            referrer_code = referrer.code
        else:
            referrer_code = None
 
        # Add the referral code to the context
        try: 
            context['referral_code'] = referral_code.code
        except AttributeError:
            context['referral_code'] = None
        
        # Add the referrer code to the context
        try: 
            context['referrer_code'] = referrer_code
        except AttributeError:
            context['referrer_code'] = None

        
        # Retrieve all referrals made by the logged-in user
        referred_users = []

        referral = None
        try:
            # Recupera tutti i Referral dell'utente autenticato
            referral = Referral.objects.filter(referrer=user).first() 
            print(referral)
            
        except Exception:
            referrer = None
        
        if referral != None:
            # Itera sui Referral e aggiungi gli utenti collegati alla lista
            for referred in referral.referred.all():
                referred_users.append(referred)  # Usa .all() per ottenere gli oggetti collegati

            # Debug: Stampa gli utenti invitati
            print("Final referred users list:", referred_users)
            # Debug: Print the final list of referred users
            print("Final Referred Users:", referred_users)

            # Pass the referred users to the context
            context['referred_users'] = referred_users

        referreds = []
        tree_referred = get_tree_referred(user, level=0)
        list_referred = tree_to_list(tree_referred, referreds)
        
        investor_accounts = []
        for referred_item in list_referred:
            referred_id = referred_item.get('id')
            referred_user = User.objects.filter(user=referred_id).first()
            referred = Profile.objects.filter(user=referred_user).first()
            profile = None
            transactions = ReferralTransaction.objects.filter(referred_user=referred.id)
            if len(transactions)>0:
                investor_accounts.append(referred_item)
        print(tree_referred)
        print(list_referred)
        print(investor_accounts)
        context['my_network'] = investor_accounts+referreds
        
        return context
    
@method_decorator(login_required, name='dispatch')
class WithdrawalView(TemplateView):
    template_name = 'dashboard/withdrawals.html'


class UserReferredLevelView(View):
    def get(self, request, *args, **kwargs):
        user=self.request.user

        # Ottieni il primo referral dell'utente
        if user.is_authenticated:
            referral = Referral.objects.filter(referrer=user).first()
        else: 
            referral = None

        if not referral:
            return JsonResponse({'error': 'No referrals found for this user'}, status=400)

        try:
            user_data = []

            # Itera su tutti gli utenti che sono stati referenziati direttamente da te
            for referred in referral.referred.all():
                # Calcola il livello di ogni utente ricorsivamente
                level = calculate_user_level(user)

                user_to_add = {
                    "first_name": referred.first_name,
                    "last_name": referred.last_name,
                    "username": referred.username,
                    "level": level,
                }
                print(user_to_add)
                user_data.append(user_to_add)

            # Restituisci i dati dei tuoi invitati con il loro livello calcolato
            return JsonResponse(user_data, safe=False)

        except Referral.DoesNotExist:
            return JsonResponse({'error': 'Referral record not found'}, status=400)

#####################
# Campaign          #
#####################
class ParticipateCampaignView(View):
    def post(self, request, *args, **kwargs):
        campaign_id = request.POST.get('campaign_id')
        try:
            campaign = ReferralCampaign.objects.get(id=campaign_id)

            # Logica per associare l'utente alla campagna (da implementare secondo le esigenze)
            # Ad esempio, associamo l'utente alla campagna

            return JsonResponse({'success': True})
        except ReferralCampaign.DoesNotExist:
            return JsonResponse({'success': False}, status=400)

def get_user_table(request):
    #user = User.objects.get(user=request.user)
    referral = Referral.objects.filter(user=request.user).first()

    # Otteniamo tutti gli utenti
    users = User.objects.all()
    
    user_data = []
    for user in users:
        # Calcoliamo il livello dell'utente ricorsivamente
        level = calculate_user_level(user)

        user_data.append({
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "level": level,
        })
    print(user_data)
    return JsonResponse(user_data, safe=False)


def privacyPolice(request):
    return render(request, 'dashboard/privacy_policy.html')

def termService(request):
    return render(request, 'dashboard/terms_of_service.html')