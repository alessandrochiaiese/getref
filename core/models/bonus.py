from django.db import models

class Bonus(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    program_id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    type = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    value = models.DecimalField(primary_key=True, blank=False, null=False)  # Valore numerico, generalmente con decimali
    min_referrals_required = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    bonus_date = models.DateTimeField(primary_key=True, blank=False, null=False)  # Data di creazione o modifica dell'entita
    expiry_date = models.DateTimeField(primary_key=True, blank=False, null=False)  # Data di creazione o modifica dell'entita
    max_usage = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    eligibility_criteria = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo

    def __str__(self):
        return str(self.id)  # Mostra il primo attributo come rappresentazione
