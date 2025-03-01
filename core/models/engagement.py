from django.db import models

class Engagement(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    link_id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    participant_id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    email_opened = models.CharField(primary_key=True, blank=False, null=False)  # Indirizzo email dell'utente
    email_clicked = models.CharField(primary_key=True, blank=False, null=False)  # Indirizzo email dell'utente
    social_share_count = models.IntegerField(primary_key=True, blank=False, null=False)  # Valore numerico intero, utilizzato per contare o classificare
    last_interaction_date = models.DateTimeField(primary_key=True, blank=False, null=False)  # Data di creazione o modifica dell'entita

    def __str__(self):
        return str(self.id)  # Mostra il primo attributo come rappresentazione
