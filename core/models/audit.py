from django.db import models

class Audit(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    participant_id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    action_taken = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    action_date = models.DateTimeField(primary_key=True, blank=False, null=False)  # Data di creazione o modifica dell'entita
    ip_address = models.CharField(primary_key=True, blank=False, null=False)  # Valore di testo, descrizione o nome dell'entita
    device_info = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    location = models.CharField(primary_key=True, blank=False, null=False)  # Valore di testo, descrizione o nome dell'entita

    def __str__(self):
        return str(self.id)  # Mostra il primo attributo come rappresentazione
