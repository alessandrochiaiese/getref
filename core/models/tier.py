from django.db import models

class Tier(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    program_id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    tier_name = models.CharField(primary_key=True, blank=False, null=False)  # Valore di testo, descrizione o nome dell'entita
    min_sales = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    commission_rate = models.DecimalField(primary_key=True, blank=False, null=False)  # Valore numerico, generalmente con decimali
    benefits = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    access_level = models.IntegerField(primary_key=True, blank=False, null=False)  # Valore numerico intero, utilizzato per contare o classificare
    next_tier_threshold = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    expiration_date = models.DateTimeField(primary_key=True, blank=False, null=False)  # Data di creazione o modifica dell'entita

    def __str__(self):
        return str(self.id)  # Mostra il primo attributo come rappresentazione
