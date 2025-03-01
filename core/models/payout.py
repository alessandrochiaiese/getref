from django.db import models

class Payout(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    participant_id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    amount = models.DecimalField(primary_key=True, blank=False, null=False)  # Valore numerico, generalmente con decimali
    currency = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    payout_date = models.DateTimeField(primary_key=True, blank=False, null=False)  # Data di creazione o modifica dell'entita
    payout_method = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    status = models.CharField(primary_key=True, blank=False, null=False)  # Stato o condizione dell'entita, ad esempio attivo o in corso
    transaction_id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    processing_fee = models.DecimalField(primary_key=True, blank=False, null=False)  # Valore numerico, generalmente con decimali
    net_amount = models.DecimalField(primary_key=True, blank=False, null=False)  # Valore numerico, generalmente con decimali
    provider = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita

    def __str__(self):
        return str(self.id)  # Mostra il primo attributo come rappresentazione
