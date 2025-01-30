from django.db import models
from django.utils.translation import gettext_lazy as _

class AffiliateCommission(models.Model):
    affiliates = models.ManyToManyField('Affiliate', verbose_name=_("Affiliates"), related_name='affiliate_commission_affiliates')
    programs = models.ManyToManyField('AffiliateProgram', verbose_name=_("Programs"), related_name='affiliate_commission_programs')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Amount"))
    currency = models.CharField(max_length=10, verbose_name=_("Currency"))
    date_awarded = models.DateField(verbose_name=_("Date Awarded"))
    status = models.CharField(max_length=50, verbose_name=_("Status"))
    approved_by = models.CharField(max_length=255, verbose_name=_("Approved By"))
    commission_type = models.CharField(max_length=50, verbose_name=_("Commission Type"))
    description = models.TextField(blank=True, verbose_name=_("Description"))
    tier = models.CharField(max_length=50, verbose_name=_("Tier"))
    
    class Meta:
        ordering = ['-date_awarded']
        verbose_name = "Affiliate Commission"
        verbose_name_plural = "Affiliate Commissions"
