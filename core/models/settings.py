from django.db import models

class Settings(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    participant_id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    preferred_currency = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    preferred_payment_method = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    payout_schedule = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    notification_preference = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    dashboard_layout = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    auto_share_setting = models.CharField(primary_key=True, blank=False, null=False)  # Collezione di elementi, generalmente oggetti o valori
    social_share_message = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo

    def __str__(self):
        return str(self.id)  # Mostra il primo attributo come rappresentazione
