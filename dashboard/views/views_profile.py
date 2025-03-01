
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string 
from django.utils.decorators import method_decorator 
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.edit import UpdateView 
from dashboard.utils import get_tree_referred, tree_to_list
from dashboard.models import *
from getref.settings import DOMAIN
from referral.models import *
from dashboard.forms import * 

#####################
#     Profile       #
#####################
@method_decorator(login_required, name='dispatch')
class ProfileView(UpdateView):
    model = get_user_model()  # Usa il modello User di default
    form_class = UpdateUserForm
    template_name = 'core/profile.html'
    success_url = reverse_lazy('core_profile')

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

        # Add the profile form to the context
        context['profile_form'] = UpdateProfileForm(instance=profile)

        # Add the profile form to the context
        context['profile_base_form'] = UpdateBaseProfileForm(instance=profile)

        # Add the referral code to the context
        context['referral_code'] = referral_code.code if referral_code else None

        # Add the referrer code to the context
        context['referrer_code'] = referrer_code.code if referrer_code else None
        context['referrer_first_name'] = referrer.first_name if referrer else ""
        context['referrer_last_name'] = referrer.last_name if referrer else ""
        context['referrer_username'] = referrer.username if referrer else ""
        context['referrer_name'] = f"{referrer.first_name} {referrer.last_name}" if referrer else ""
  
        context['referral_unique_url'] = referral_code.unique_url if referral_code else None
        
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
    
    def form_valid(self, form):
        user = self.request.user
        profile = Profile.objects.filter(user=user).first()
        
        if not profile:
            messages.error(self.request, 'Profile not found for the current user.')
            return self.form_invalid(form)

        # Gestisci separatamente il profilo
        profile_form = UpdateProfileForm(self.request.POST, self.request.FILES, instance=profile)
        profile_base_form = UpdateBaseProfileForm(self.request.POST, instance=profile)

        if not profile_form.is_valid():
            print("Profile Form Errors:", profile_form.errors)
            messages.error(self.request, 'There was an error updating your profile.')
            return self.form_invalid(form)

        if not profile_base_form.is_valid():
            print("Profile Base Form Errors:", profile_base_form.errors)
            messages.error(self.request, 'There was an error updating your profile.')
            return self.form_invalid(form)

        # Salvataggio dei form
        profile_form.save()  # Salva i dati del profilo
        profile_base_form.save()  # Salva i dati del profilo base
        form.save()  # Salva i dati utente

        # Aggiungi un messaggio di successo
        messages.success(self.request, 'Your profile and account information were updated successfully.')

        return super().form_valid(form)

#####################
#    Enterprise     #
#####################
@method_decorator(login_required, name='dispatch')
class EnterpriseListView(ListView):
    model = ProfileBusiness
    template_name = 'dashboard/enterprise/enterprise_list.html'
    context_object_name = 'profiles'  # Nome del contesto nel template
    paginate_by = 10  # Paginazione dei risultati

    def get_queryset(self):
        # Se l'utente è un admin, mostra tutte le aziende
        if self.request.user.is_superuser:
            return ProfileBusiness.objects.all()
        
        # Se l'utente non è admin, mostra solo le aziende che ha creato
        return ProfileBusiness.objects.filter(user=self.request.user)

@method_decorator(login_required, name='dispatch')
class EnterpriseCreateView(CreateView):
    model = ProfileBusiness
    form_class = EnterpriseForm
    template_name = 'dashboard/enterprise/create_enterprise.html'
    success_url = reverse_lazy('core_profile')  # Redirige alla pagina del profilo dell'utente o a un'altra pagina di successo

    def form_valid(self, form):
        # Se vuoi eseguire operazioni extra quando il form è valido
        code = get_random_string(length=8).upper()
        form.instance.user = self.request.user
        form.instance.unique_url = f"{DOMAIN}/enterprise/?code={code}"
        form.instance.code = code
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Aggiungi nuovo profilo aziendale"
        return context
    
@method_decorator(login_required, name='dispatch')
class EnterpriseUpdateView(UpdateView):
    model = ProfileBusiness
    form_class = EnterpriseForm
    template_name = 'dashboard/enterprise/create_enterprise.html'
    success_url = reverse_lazy('core_profile')

    def get_object(self, queryset=None):
        # Puoi gestire l'oggetto in base alla logica che desideri, per esempio
        # Restituisci un oggetto ProfileBusiness specifico per l'utente corrente
        return ProfileBusiness.objects.get(id=self.kwargs['pk'])

    def form_valid(self, form):
        # Operazioni personalizzate quando il form è valido
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Modifica profilo aziendale"
        return context


@method_decorator(login_required, name='dispatch')
class EnterpriseDetailView(DetailView):
    model = ProfileBusiness
    template_name = 'dashboard/enterprise/enterprise_detail.html'
    context_object_name = 'profile'  # Nome del contesto nel template

    def get_object(self, queryset=None):
        # Recupera il profilo aziendale in base all'ID passato nell'URL
        return ProfileBusiness.objects.get(id=self.kwargs['pk'])
