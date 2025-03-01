from django.db import models

class Campaign(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    program_id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    name = models.CharField(primary_key=True, blank=False, null=False)  # Valore di testo, descrizione o nome dell'entita
    start_date = models.DateTimeField(primary_key=True, blank=False, null=False)  # Data di creazione o modifica dell'entita
    end_date = models.DateTimeField(primary_key=True, blank=False, null=False)  # Data di creazione o modifica dell'entita
    goal = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    budget = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    spending_to_date = models.DateTimeField(primary_key=True, blank=False, null=False)  # Data di creazione o modifica dell'entita
    target_audience = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo

    def __str__(self):
        return str(self.id)  # Mostra il primo attributo come rappresentazione
