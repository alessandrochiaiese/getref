from django.db import models
from django.utils.translation import gettext_lazy as _

class AffiliatePayout(models.Model):
    affiliates = models.ManyToManyField('Affiliate', verbose_name=_("Affiliates"), related_name='affiliate_payout_affiliates') 
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Amount"))
    currency = models.CharField(max_length=10, verbose_name=_("Currency"))
    payout_date = models.DateField(verbose_name=_("Payout Date"))
    payout_method = models.CharField(max_length=50, verbose_name=_("Payout Method"))
    payout_status = models.CharField(max_length=50, verbose_name=_("Payout Status"))
    transaction = models.ForeignKey('AffiliateTransaction', on_delete=models.CASCADE, verbose_name=_("Transaction"))
    processing_fee = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Processing Fee"))
    net_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Net Amount"))
    payout_provider = models.CharField(max_length=50, verbose_name=_("Payout Provider"))

    class Meta:
        ordering = ['-payout_date']
        verbose_name = "Affiliate Payout"
        verbose_name_plural = "Affiliate Payouts"
