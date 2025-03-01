from django.db import models

class Participant(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    user_id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    program_id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    status = models.CharField(primary_key=True, blank=False, null=False)  # Stato o condizione dell'entita, ad esempio attivo o in corso
    total_earnings = models.DecimalField(primary_key=True, blank=False, null=False)  # Valore numerico, generalmente con decimali
    account_balance = models.IntegerField(primary_key=True, blank=False, null=False)  # Valore numerico intero, utilizzato per contare o classificare
    date_joined = models.DateTimeField(primary_key=True, blank=False, null=False)  # Data di creazione o modifica dell'entita
    last_login = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    referral_source = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo

    def __str__(self):
        return str(self.id)  # Mostra il primo attributo come rappresentazione
