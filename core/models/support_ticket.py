from django.db import models

class SupportTicket(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    participant_id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    ticket_number = models.IntegerField(primary_key=True, blank=False, null=False)  # Valore numerico intero, utilizzato per contare o classificare
    subject = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    description = models.CharField(primary_key=True, blank=False, null=False)  # Valore di testo, descrizione o nome dell'entita
    status = models.CharField(primary_key=True, blank=False, null=False)  # Stato o condizione dell'entita, ad esempio attivo o in corso
    date_created = models.DateTimeField(primary_key=True, blank=False, null=False)  # Data di creazione o modifica dell'entita
    date_closed = models.DateTimeField(primary_key=True, blank=False, null=False)  # Data di creazione o modifica dell'entita
    priority = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    assigned_agent = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo

    def __str__(self):
        return str(self.id)  # Mostra il primo attributo come rappresentazione
