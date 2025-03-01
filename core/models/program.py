from django.db import models

class Program(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    name = models.CharField(primary_key=True, blank=False, null=False)  # Valore di testo, descrizione o nome dell'entita
    description = models.CharField(primary_key=True, blank=False, null=False)  # Valore di testo, descrizione o nome dell'entita
    program_type = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    reward_type = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    reward_value = models.DecimalField(primary_key=True, blank=False, null=False)  # Valore numerico, generalmente con decimali
    currency = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    commission_rate = models.DecimalField(primary_key=True, blank=False, null=False)  # Valore numerico, generalmente con decimali
    min_payout_threshold = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    max_payout_limit = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    date_created = models.DateTimeField(primary_key=True, blank=False, null=False)  # Data di creazione o modifica dell'entita
    is_active = models.BooleanField(primary_key=True, blank=False, null=False)  # Stato del flag, 1 per vero, 0 per falso
    duration = models.DecimalField(primary_key=True, blank=False, null=False)  # Percentuale o tasso di interesse applicato
    allowed_regions = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    target_industry = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo

    def __str__(self):
        return str(self.id)  # Mostra il primo attributo come rappresentazione
