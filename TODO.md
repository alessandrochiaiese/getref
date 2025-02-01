
TODO:
[X] Adjust Subscriptions (Plan subscription  system)
[X] Adjust Accounts (Oauth System)
[X] Adjust Core (login System)
[X] Adjust funzione Logout
[X] Adjust Copy referral code
[X] Create table into referred profile with levels (1, 3, 4, ..., 6 livello)
[X] Create Product model 
[X] Create Order model
[X] Creare page to create view products
[X] Creare page to create view orders

[/] Auth Github (NOT USEFUL)
[/] Auth Google
[ ] Wordpress + Stripe Plugin



03.01.2025
[X] Page login Style (margin or paggind)
[X] Page Register Style (margin or paggind)
[X] Page Base Auth Style (margin or paggind)
[X] Button Copy Referral Code with icon and js in Dashboard Page
[X] Button Copy Referral Code with icon and js in Profile Page
[X] Button Copy Referral Link with icon and js in Profile Page
[X] Input Field to upload in Profile Page with Bootstrap
[X] Populate Regions, Provinces, Municipalities
[X] Populate Sectors
[X] Signup Enterprise Page

23.01.2025
[X] Move important models and middleware from referral to dashboard
[X] Delete referral app
[X] Test
[X] Populate Regions
[X] Modify field regions into TextField
[X] Add in admin.py ProfileBusiness
[X] ProfileBusiness can be saved in admin, but not into /create_enterprise/
[X] Create Read Update Delete Enterprise created by user. Admin can see all
[X] Referral Code in Dashboard [DON'T WORK]
[X] Referral COde needs to be dispayed as URL
[X] Statical [DON'T WORK]
29.01.2025
[X] nella dashboard la tabella "I miei invitati" non funziona, mancano le importazioni di referral.models
[X] APPEND_SLASH=True
[X] Nella pagina profile, dove sta scritto "Ti sei registrato con il codice referral:" bisognerebbe mettere: "Sei stato invitato da: {Nome} e {Cognome} (Codice Referral)"
[X] Creare Middleware che se non sei admin e sbagli endpoint deve uscire la pagina 404 Not Found
[/] Internationalization and localization
[X] la tabella "I miei invitati" in dashboard potrebbe essere spostata in Referred Accounts nella sidebar
N.B. In realtà stanno in My IBs
[X] La tabella "I miei invitati" potrebbe essere chiamata intitolata "La mia rete"
Accounts>Accounts (Nuova voce), nella sidebar
[X] per endpoint "referral-code/<Codice>/" serve usare gli ARGS di GET (request.GET)
N.B.:
in urls.py:
    path('register/', RegisterView.as_view(), name='core_register'),    
    path('referral-code/<str:referral_code>/', ReferralRedirectView.as_view(), name='referral_redirect'),
    path('register/<str:referral_code>/', RegisterView.as_view(), name='core_register_with_referral'),

in views_accounts.py:
class ReferralRedirectView(View):
    def get(self, request, *args, **kwargs):
        referral_code = kwargs.get('referral_code') #path('referral/<str:referral_code>/')
        #referral_code = request.GET.get('referral_code') #path('referral/')

class RegisterView(View):
    def get(self, request, *args, **kwargs):
        referral_code_used = kwargs.get('referral_code')  # Codice referral da URL


[X] API Documentation non funziona
[X] Aggiustare Middleware di Referral Sys. referral_audit_middleware.py
Errore:
IntegrityError at /api/v0/referral/
null value in column "ip_address" of relation "referral_referralaudit" violates not-null constraint
DETAIL:  Failing row contains (25, /api/v0/referral/, 2025-01-29, null, Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KH..., <IP>, null).
[X] Modify button in detail enterprise




30.01.2025
[ ] Create Page to create and manage API KEY
[ ] Make all Html with Internationalization and Localization
[ ] The pages of Affiliates and Referral Systems needs restyling
[ ] Create App to subscription for different plan about API
[ ]
[ ]
[ ] Nella sidebar i dropdown devono avere gli angoli inferiori a destra e sinistra arrotandati come quelli degli angoli opposti
[ ] nel register page campo referral code

[ ] Flash List in Dashboard [DON'T DESERVE]
[ ] Create Affiliation Program and Campaign [DON'T DESERVE]

[ ] Track payment (Debit card In o OUT), se è completato è cliente 100% quindi la commissione va a chi l ha invitato
[ ] Creazione di Form a fasi tipo 4 fasi, la prima registrazione, seconda registrazione dell'azienda, terza per la aggiunta di un metodo di pagamento
[ ] sistema dell'email, anche nela registrazione per confermare, ma anche un email del cliente prerogativa per chiedere di fare un azione un pagamento o per le condizioni da confermare

[ ] Plan Subscription for API Services (Affiliate & Referral)
[ ] Stripe, Create i prodotti o servizi (piani di affiliazione sys e piani di referral sys)




USEFUL LINK:
https://aisaastemplate.com/blog/django-stripe-integration/
https://github.com/testdrivenio/django-stripe-checkout
https://github.com/sobit-nep/Django-User-Registration-with-Email-Confirmation-Link-Verification
