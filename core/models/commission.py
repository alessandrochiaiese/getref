from django.db import models

class Commission(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    participant_id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    program_id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    amount = models.DecimalField(primary_key=True, blank=False, null=False)  # Valore numerico, generalmente con decimali
    currency = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    date_awarded = models.DateTimeField(primary_key=True, blank=False, null=False)  # Data di creazione o modifica dell'entita
    status = models.CharField(primary_key=True, blank=False, null=False)  # Stato o condizione dell'entita, ad esempio attivo o in corso
    approved_by = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    type = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    description = models.CharField(primary_key=True, blank=False, null=False)  # Valore di testo, descrizione o nome dell'entita
    tier = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo

    def __str__(self):
        return str(self.id)  # Mostra il primo attributo come rappresentazione
