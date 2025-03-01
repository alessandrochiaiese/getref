from django.db import models

class Conversion(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    link_id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    referred_user_id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    conversion_date = models.DateTimeField(primary_key=True, blank=False, null=False)  # Data di creazione o modifica dell'entita
    conversion_value = models.DecimalField(primary_key=True, blank=False, null=False)  # Valore numerico, generalmente con decimali
    status = models.CharField(primary_key=True, blank=False, null=False)  # Stato o condizione dell'entita, ad esempio attivo o in corso
    reward_issued = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    source = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    type = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo

    def __str__(self):
        return str(self.id)  # Mostra il primo attributo come rappresentazione
