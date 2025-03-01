from django.db import models

class Performance(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    participant_id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    period = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo
    total_clicks = models.DecimalField(primary_key=True, blank=False, null=False)  # Valore numerico, generalmente con decimali
    total_conversions = models.DecimalField(primary_key=True, blank=False, null=False)  # Valore numerico, generalmente con decimali
    conversion_rate = models.DecimalField(primary_key=True, blank=False, null=False)  # Valore numerico, generalmente con decimali
    total_earnings = models.DecimalField(primary_key=True, blank=False, null=False)  # Valore numerico, generalmente con decimali
    average_order_value = models.DecimalField(primary_key=True, blank=False, null=False)  # Valore numerico, generalmente con decimali
    refund_rate = models.DecimalField(primary_key=True, blank=False, null=False)  # Valore numerico, generalmente con decimali
    customer_lifetime_value = models.DecimalField(primary_key=True, blank=False, null=False)  # Valore numerico, generalmente con decimali
    top_product = models.CharField(primary_key=True, blank=False, null=False)  # Descrizione generica dell'attributo

    def __str__(self):
        return str(self.id)  # Mostra il primo attributo come rappresentazione
