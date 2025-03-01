from django.db import models

class Affiliate(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    user_id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    name = models.CharField(primary_key=True, blank=False, null=False)  # Valore di testo, descrizione o nome dell'entita
    email = models.CharField(primary_key=True, blank=False, null=False)  # Indirizzo email dell'utente
    phone = models.CharField(primary_key=True, blank=False, null=False)  # Numero di telefono dell'utente
    date_joined = models.DateTimeField(primary_key=True, blank=False, null=False)  # Data di creazione o modifica dell'entita
    status = models.CharField(primary_key=True, blank=False, null=False)  # Stato o condizione dell'entita, ad esempio attivo o in corso
    total_earnings = models.DecimalField(primary_key=True, blank=False, null=False)  # Valore numerico, generalmente con decimali
    country = models.IntegerField(primary_key=True, blank=False, null=False)  # Valore numerico intero, utilizzato per contare o classificare
    profile_picture = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    account_balance = models.IntegerField(primary_key=True, blank=False, null=False)  # Valore numerico intero, utilizzato per contare o classificare
    last_login = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    referral_source = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo

    def __str__(self):
        return str(self.id)  # Mostra il primo attributo come rappresentazione
