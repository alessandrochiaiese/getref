
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
[X] Make all Html with Internationalization and Localization
[ ] Translation of msgid in msgstr in .po files 
[ ] The pages of Affiliates and Referral Systems needs restyling
[ ] Create App to subscription for different plan about API
[ ]
[ ]
[ ] Nella sidebar i dropdown devono avere gli angoli inferiori a destra e sinistra arrotandati come quelli degli angoli opposti
[ ] nel register page campo referral code
[X] Incomplete Registration page not work 
[ ] Flash List in Dashboard [DON'T DESERVE]
[ ] Create Affiliation Program and Campaign [DON'T DESERVE]

[ ] Track payment (Debit card In o OUT), se è completato è cliente 100% quindi la commissione va a chi l ha invitato
[ ] Creazione di Form a fasi tipo 4 fasi, la prima registrazione, seconda registrazione dell'azienda, terza per la aggiunta di un metodo di pagamento
[ ] sistema dell'email, anche nela registrazione per confermare, ma anche un email del cliente prerogativa per chiedere di fare un azione un pagamento o per le condizioni da confermare

[/] Plan Subscription for API Services (Affiliate & Referral)
[ ] Stripe, Create i prodotti o servizi (piani di affiliazione sys e piani di referral sys)


25.02.2025



*_affiliate.py
*_audit.py
*_bonus.py
*_campaign.py
*_commission.py
*_conversion.py
*_country.py          DELETE
*_custom_order.py     DELETE
*_engagement.py
*_link.py
*_notification.py
*_order_item.py       DELETE
*_order.py            DELETE
*_participant.py
*_payment_method.py
*_payout.py
*_performance.py
*_price.py            DELETE
*_product_tag.py      DELETE
*_product.py          DELETE
*_profile.py          DELETE
*_program.py
*_referral_code.py
*_referral_level.py
*_region.py           DELETE
*_reward.py
*_settings.py
*_stats.py
*_support_ticket.py
*_tier.py
*_transaction.py
*_user.py             DELETE





01.03.2025
o Utente   o Business

register/
register/business/

[] in Register Page aggiungere i tab per 2 entità: utente e azienda
[] considera di creare due Register Page: utente e azienda
[\] in Profile Page si potrebbe aggiungere i tab: se è utente niente tab perche ci saranno solo dati , invece
[] in Profile il caricamento dell'immagine da errore
[X] Enterprise list potrebbe essere visualizzata sotto forma di tabella ( MY NETWORK)
[] Verificare che il link promozionale del prodotto permettti di tracciare la vendita del prodotto con eventuali bonus e commissioni
Bonus i primi 5 invitati che fanno ognuno un acquisto
Commissione 15% CPA
[\] Modify APIView Authentication
[X] Campaign and Program in home
[X] a non far funzionare il referral invitation è in dashboard/urls.py:

    path('referral-code/', ReferralRedirectView.as_view(), name='referral_redirect'),
    perchè referral-code/ è stato sostituito con en/register/?code=

    (SI E PER QUESTO MOTIVO QUI)
[X] controlla perche utente non riesce a registrarsi sotto l utente che invita
[X] controlla i due tipi di referral coding (utente e azienda)
[X] quando si incolla url invito azienda compare il messagio Codice referral non è valido. (vedi in views_accounts.py a rigo 99:                 messages.warning(request, 'Il codice referral non è valido.'))
[X] Nella mia rete bisogna vedere gli utenti referenziati, gli amministratori aziende clienti registrati, aziende
quindi magare fare la mia rete e la mia rete di aziende 
[X] in my_promotions bisogna definire Price: Unkown price
[X] definire la pagina settings per:
- impostare la lingua
- 


[] inserire Privacy Policy e Terms of Service (quando disponibile o  con IUBENDA)
[] 
[] 
[] 






[X] il link di referral utente e azienda dovrebbero essere piu brevi (in urls.py gli endpoint andrebbero rivisti e in views_profile.py l'endpoint per invitare l azienda e in view_accounts.py per invitare l'utente, (per il primo forse si potrebbe usare per internderci /e/ e invece per l'utente si potrebbe usare /)) 



[\] Fare ultime modifiche alle API core (affiliate, referral), riguardo i valori di self.request in views per recuperare IP e dispositivo (che mancano probabilmente non ricordo)
[] cancella app affiliate e referral e quindi modifica gli import nella logica e eventualmente il nome dell'instanza che non inizieranno più con Affiliate_ o Referral_
[\] collega il pagamento di un plans con le API (core)


N.B.: 
- quando invito azienda a registrarsi funziona (OK)
- quando invito utente a registrarsi non funziona (TODO)
- ReferralLevel non viene mai utilizzato nella logica (BHO NON SO SE è PIU UTILE)
- 


07.03.2025

[X] quando invito con il link:
- /c/?code=FHGRTED e si prova a registrasi come azienda non va bene
- /e/?code=FHGRTED e si prova a registrasi come utente non va bene

[] quando si crea un azienda con /create-enterprise/ si popolano i campi di ProfileBusiness(Business) con link referenziale /e/?code=HGTFYDS ma quando uso questo link per registrarmi come azienda (apparte l'errore precedente della todolist) i campi azienda dovrebbero essere già popolati

[\] quando da utente normale vado in /profile/ ci sono anche i campi aziendali 
[] quando uso:
- /promote/<promo-link> 
- /create-checkout-session/
- /webhook/
molte delle logiche comuni dovrebbero ripetersi
[]
[]
[]
[]
[]
[]





21.03.2025
[] Bottone buy in products non traccia commissioni a referrer (tramite referral code)
[] Bottone Promote da eliminare o commentare
[] Redirect Promotion da eliminare o commentare
[] Quando compri, da cliente, un prodotto, arriva la commissione al referrer
[] Product Detail
[] Prodotti Tabellati o doppia visione (card e tabella)	









USEFUL LINK:
https://aisaastemplate.com/blog/django-stripe-integration/
https://github.com/testdrivenio/django-stripe-checkout
https://github.com/sobit-nep/Django-User-Registration-with-Email-Confirmation-Link-Verification
