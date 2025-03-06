
import datetime
from urllib.parse import urlencode
from django.conf import settings
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView 
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy 
from django.utils.crypto import get_random_string 
from dashboard.models import *   
from getref.settings import DOMAIN #, EMAIL_HOST_USER
from referral.models import *   
from dashboard.forms import * 
import logging

logger = logging.getLogger(__name__)



#####################
# Register & Login  #
#####################
class EnterpriseRedirectView(View):
    def get(self, request, *args, **kwargs):
        referral_code = self.request.GET.get('code')

        # Verifica che il codice referral esista
        try:
            referral = ProfileBusiness.objects.get(code=referral_code)
            # Imposta un flag nel request per sapere se è EnterpriseRedirectView
            request.session['is_enterprise_redirect'] = True
            request.session['is_referral_redirect'] = False
            # Redirect alla vista di registrazione, passando il codice referral come parte dell'URL
            #return redirect(reverse('core_register', args=[referral_code]))

            # Costruisci l'URL con il parametro di query
            url = reverse('core_register')  # Ottieni la base dell'URL
            query_string = urlencode({'code': referral_code})  # Aggiungi il parametro alla query
            full_url = f'{url}?{query_string}'  # Combina l'URL con la query

            return HttpResponseRedirect(full_url)  # Fai il redirect alla nuova URL
        except ProfileBusiness.DoesNotExist:
            messages.warning(request, 'Codice referral azienda non valido o inattivo.')
            # Se il codice referral non è valido, reindirizza ad una pagina di errore o alla home
            return redirect('/')
        
class ReferralRedirectView(View):
    def get(self, request, *args, **kwargs):
        referral_code = self.request.GET.get('code')

        # Verifica che il codice referral esista
        try:
            referral = ReferralCode.objects.get(code=referral_code, status='active')
            # Imposta un flag nel request per sapere se è ReferralRedirectView
            request.session['is_enterprise_redirect'] = False
            request.session['is_referral_redirect'] = True
            # Redirect alla vista di registrazione, passando il codice referral come parte dell'URL
            #return redirect(reverse('core_register', args=[referral_code]))

            # Costruisci l'URL con il parametro di query
            url = reverse('core_register')  # Ottieni la base dell'URL
            query_string = urlencode({'code': referral_code})  # Aggiungi il parametro alla query
            full_url = f'{url}?{query_string}'  # Combina l'URL con la query

            return HttpResponseRedirect(full_url)  # Fai il redirect alla nuova URL
        except ReferralCode.DoesNotExist:
            messages.warning(request, 'Codice referral utente non valido o inattivo.')
            # Se il codice referral non è valido, reindirizza ad una pagina di errore o alla home
            return redirect('/')

class RegisterView(View):
    form_class = RegisterForm
    business_form_class = BusinessForm
    initial = {'key': 'value'}
    template_name = 'core/register.html'
    success_url = '/login/'  # Dopo il successo della registrazione, reindirizza alla pagina di login
 
    def dispatch(self, request, *args, **kwargs):
        # Redirect alla home se l'utente è già autenticato
        if request.user.is_authenticated:
            return redirect('/')

        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        # Verifica se c'è un referral code nei parametri GET
        referral_code_used = self.request.GET.get('code')
        form = self.form_class(initial=self.initial)
        business_form = self.business_form_class(initial=self.initial)

        #if referral_code_used:
        #    try:
        #        referral_code = ReferralCode.objects.get(code=referral_code_used, status="active")
        #        print(form.fields)
        #        # Imposta il referral_code nel form (se necessario)
        #        # form.fields['referral_code'].initial = referral_code.code
        #    except ReferralCode.DoesNotExist:
        #        messages.warning(request, 'Il codice referral non è valido.')

        response = render(request, self.template_name, {
            'form': form,
            'business_form': business_form,
        })

        if referral_code_used:
            response.set_cookie('code', referral_code_used, max_age=60*60*24*30) # 30 giorni

        return response
    
    def post(self, request, *args, **kwargs):   
        referral_code_used = self.request.POST.get('code') or request.COOKIES.get('code')
        form = self.form_class(self.request.POST)
        account_type = request.POST.get('account_type')  # Ottieni il tipo di account selezionato
        business_form = None
        
        if account_type == 'business':
            business_form = self.business_form_class(request.POST, request.FILES)

        if form.is_valid() and (not business_form or business_form.is_valid()):
            user = form.save()
            referrer_code = None

            if account_type == 'business' and business_form:
                business = business_form.save(commit=False)
                business.save()
                
                profile = Profile.objects.get(user=user)
                profile.business = business
                profile.save()

            # Gestione codice referral per aziende
            is_enterprise_redirect = request.session.get('is_enterprise_redirect', False)
            is_referral_redirect = request.session.get('is_referral_redirect', False)

            # Se il nuovo utente ha usato un codice referral
            if referral_code_used:
                if is_enterprise_redirect and not is_referral_redirect:
                    # Trattamento codice referral aziendale
                    try:
                        profile_business = ProfileBusiness.objects.get(code=referral_code_used)
                        profile_business.user_ower = user
                        profile_business.status = 'active'
                        profile_business.save()
                        # Recupera utente che ha invitato un'azienda a registrarsi
                        referrer=profile_business.user
                        print(f"ProfileBusiness aggiornato per {user.username}")
                    except ProfileBusiness.DoesNotExist:
                        messages.warning(request, 'Codice referral azienda non valido.')
                elif is_referral_redirect and not is_enterprise_redirect:
                    # Trattamento codice referral utente
                    try:
                        referral_code = ReferralCode.objects.get(code=referral_code_used, status="active")
                        # Recupera utente che ha invitato un utente a registrarsi
                        referrer = referral_code.user
                        referral_code.referred_user_count += 1
                        referral_code.save()
                        messages.success(request, f"Registrazione completata! Sei stato invitato da {referrer.username}.")
                    except ReferralCode.DoesNotExist:
                        messages.warning(request, 'Codice referral utente non valido.')

                # Creazione o aggiornamento del record di referral
                referral, created = Referral.objects.get_or_create(referrer=referrer)
                referral.referred.add(user)

                # Rimuovi il flag dalla sessione dopo l'uso
                request.session.pop('is_enterprise_redirect', None)
                request.session.pop('is_referral_redirect', None)


            else:
                # Messaggio di successo standard se nessun referral è stato usato
                messages.success(request, 'Registrazione completata! Benvenuto.')



            # Creazione del codice referral per il nuovo utente
            code = get_random_string(length=8).upper()
            referral_program, created= ReferralProgram.objects.get_or_create(
                name="Programma Referral Premium",
                description="Programma per utenti premium",
                reward_type="Cash",
                reward_value=100.00,
                currency="EUR",
                min_referral_count=5,
                max_referrals_per_user=10,
                program_duration=365*10,  # Durata di 30 giorni
                target_industry="Getref"
            )
            # Assuming you have a list of region IDs
            region_ids = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            regions = Region.objects.filter(id__in=region_ids)

            # Now assign the regions to the allowed_regions field
            referral_program.allowed_regions.set(regions)

            referral_code = ReferralCode.objects.create(
                user=user,
                code=code,
                usage_count=0,
                status="active",
                referred_user_count=0,
                expiry_date=self.request.POST.get('expiry_date'),
                unique_url=f'{DOMAIN}/c/?code={code}' #self.request.build_absolute_uri(f'?code={code}'),
            )
            referral_conversion = ReferralConversion.objects.create(
                referral_code=referral_code,
                referred_user=user,
                conversion_date=datetime.datetime.now(),
                conversion_value=0.00,
                status="Completed",
                reward_issued=False,
                conversion_source="website",
                referral_type="Standard"
            )
            referral_engagement = ReferralEngagement.objects.create(
                referral_code=referral_code,
                user=user,
                email_opened=True,
                email_clicked=True,
                social_share_count=3,
                last_interaction_date=datetime.datetime.now(),
            )
            # Redirect al login
            response = redirect('core_login')
            response.delete_cookie('code')  # Rimuovi il cookie
            return response

        return render(request, self.template_name, {
            'form': form,
            'business_form': business_form if account_type == 'business' else None,
        })
    
# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'core/login.html'

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # login() is needed to ensure the session is saved
        login(self.request, form.get_user())
        
        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'core/password_reset.html'
    email_template_name = 'core/password_reset_email.html'
    subject_template_name = 'core/password_reset_subject.html'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('core_home')

    def form_valid(self, form):
        if not self.request:
            logger.error("Request is None in form_valid!")
            return self.form_invalid(form)

        try:
            form.save(
                request=self.request,
                from_email="EMAIL_HOST_USER",
                    extra_email_context={'domain': DOMAIN}
            )
            logger.info("Email di reset inviata con successo")
        except Exception as e:
            logger.error(f"Errore durante l'invio dell'email: {e}")
        return super().form_valid(form)
    
class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'core/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('core_home')



class LandingPageView(TemplateView):
    template_name = 'core/landing_page.html'
    

    
def custom_logout(request):
    logout(request)  # Invalidiamo la sessione dell'utente
    return redirect('core_home')  # Redirigi alla home (o a qualsiasi altra pagina)
