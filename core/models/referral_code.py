from django.db import models

class ReferralCode(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    participant_id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    program_id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    code = models.CharField(primary_key=True, blank=False, null=False)  # Codice univoco per identificare l'entita
    usage_count = models.IntegerField(primary_key=True, blank=False, null=False)  # Valore numerico intero, utilizzato per contare o classificare
    date_created = models.DateTimeField(primary_key=True, blank=False, null=False)  # Data di creazione o modifica dell'entita
    status = models.CharField(primary_key=True, blank=False, null=False)  # Stato o condizione dell'entita, ad esempio attivo o in corso
    expiry_date = models.DateTimeField(primary_key=True, blank=False, null=False)  # Data di creazione o modifica dell'entita
    referred_user_count = models.IntegerField(primary_key=True, blank=False, null=False)  # Valore numerico intero, utilizzato per contare o classificare
    unique_url = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    campaign_source = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    campaign_medium = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo

    def __str__(self):
        return str(self.id)  # Mostra il primo attributo come rappresentazione
