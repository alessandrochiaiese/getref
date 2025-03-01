from django.db import models

class Link(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    participant_id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    program_id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    url = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    click_count = models.IntegerField(primary_key=True, blank=False, null=False)  # Valore numerico intero, utilizzato per contare o classificare
    conversion_count = models.IntegerField(primary_key=True, blank=False, null=False)  # Valore numerico intero, utilizzato per contare o classificare
    date_created = models.DateTimeField(primary_key=True, blank=False, null=False)  # Data di creazione o modifica dell'entita
    last_used = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    status = models.CharField(primary_key=True, blank=False, null=False)  # Stato o condizione dell'entita, ad esempio attivo o in corso
    landing_page = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    custom_tracking_id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita

    def __str__(self):
        return str(self.id)  # Mostra il primo attributo come rappresentazione
