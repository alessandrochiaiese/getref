from django.db import models

class Stats(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    link_id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    period = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    click_count = models.IntegerField(primary_key=True, blank=False, null=False)  # Valore numerico intero, utilizzato per contare o classificare
    conversion_count = models.IntegerField(primary_key=True, blank=False, null=False)  # Valore numerico intero, utilizzato per contare o classificare
    total_rewards = models.DecimalField(primary_key=True, blank=False, null=False)  # Valore numerico, generalmente con decimali
    average_conversion_value = models.DecimalField(primary_key=True, blank=False, null=False)  # Valore numerico, generalmente con decimali
    highest_referral_earning = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo

    def __str__(self):
        return str(self.id)  # Mostra il primo attributo come rappresentazione
