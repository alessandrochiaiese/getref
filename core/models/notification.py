from django.db import models

class Notification(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    participant_id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    message = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    date_sent = models.DateTimeField(primary_key=True, blank=False, null=False)  # Data di creazione o modifica dell'entita
    is_read = models.BooleanField(primary_key=True, blank=False, null=False)  # Stato del flag, 1 per vero, 0 per falso
    priority = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    type = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    action_required = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo

    def __str__(self):
        return str(self.id)  # Mostra il primo attributo come rappresentazione
