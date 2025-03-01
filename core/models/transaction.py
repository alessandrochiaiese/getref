from django.db import models

class Transaction(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    participant_id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    link_id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    transaction_amount = models.DecimalField(primary_key=True, blank=False, null=False)  # Valore numerico, generalmente con decimali
    transaction_date = models.DateTimeField(primary_key=True, blank=False, null=False)  # Data di creazione o modifica dell'entita
    order_id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    product_id = models.IntegerField(primary_key=True, blank=False, null=False)  # Identificativo univoco dell'entita
    status = models.CharField(primary_key=True, blank=False, null=False)  # Stato o condizione dell'entita, ad esempio attivo o in corso
    payment_date = models.DateTimeField(primary_key=True, blank=False, null=False)  # Data di creazione o modifica dell'entita
    commission_rate = models.DecimalField(primary_key=True, blank=False, null=False)  # Valore numerico, generalmente con decimali
    discount_applied = models.DecimalField(primary_key=True, blank=False, null=False)  # Valore numerico, generalmente con decimali
    coupon_code = models.CharField(primary_key=True, blank=False, null=False)  # Codice univoco per identificare l'entita

    def __str__(self):
        return str(self.id)  # Mostra il primo attributo come rappresentazione
