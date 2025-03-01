from django.db import models

class PaymentMethod(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    amount = models.DecimalField(primary_key=True, blank=False, null=False)  # Valore numerico, generalmente con decimali
    description = models.CharField(primary_key=True, blank=False, null=False)  # Valore di testo, descrizione o nome dell'entita
    paid = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    user_id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita

    def __str__(self):
        return str(self.id)  # Mostra il primo attributo come rappresentazione
