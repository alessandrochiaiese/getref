from django.db import models

class ReferralLevel(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    referrer = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    referred = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    level = models.IntegerField(primary_key=True, blank=False, null=False)  # Valore numerico intero, utilizzato per contare o classificare

    def __str__(self):
        return str(self.id)  # Mostra il primo attributo come rappresentazione
