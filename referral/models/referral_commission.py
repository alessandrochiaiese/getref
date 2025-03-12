from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


User = get_user_model()

class ReferralCommission(models.Model):
    referral_code = models.ForeignKey('ReferralCode', on_delete=models.CASCADE, verbose_name=_("Referral Code"))
    referred_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Referred User"))
    
    # Commissione guadagnata
    commission_value = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name=_("Commission Value"))
    
    # Data in cui la commissione è stata guadagnata
    commission_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Commission Date"))
    
    # Stato della commissione (se è stata pagata o è in sospeso)
    status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Cancelled', 'Cancelled')
    ], default='Pending', verbose_name=_("Status"))
    
    # Evento che ha attivato la commissione (ad esempio, pagamento completato, acquisto effettuato)
    trigger_event = models.CharField(max_length=100, blank=True, verbose_name=_("Trigger Event"))
    
    # Eventuale riferimento a una transazione (per tracciare direttamente la transazione legata alla commissione)
    transaction = models.ForeignKey('ReferralTransaction', on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("Transaction ID"))
    
    # Percentuale della commissione, utile se la commissione è una percentuale sull'importo di una vendita
    commission_percentage = models.DecimalField(default=0.00, max_digits=5, decimal_places=2, null=True, blank=True, verbose_name=_("Commission Percentage"))
    
    # Data di scadenza della commissione (se applicabile, per esempio in caso di bonus con scadenza)
    expiry_date = models.DateField(default=None, null=True, blank=True, verbose_name=_("Expiry Date"))
    
    class Meta:
        verbose_name = "Referral Commission"
        verbose_name_plural = "Referral Commissions"

    def __str__(self):
        return f"Commission for {self.referral_code} - {self.commission_value}"
