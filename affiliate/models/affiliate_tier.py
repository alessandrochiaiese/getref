from django.db import models
from django.utils.translation import gettext_lazy as _

class AffiliateTier(models.Model): 
    programs = models.ManyToManyField('AffiliateProgram', verbose_name=_("Programs"), related_name='affiliate_tier_programs')
    tier_name = models.CharField(max_length=50, verbose_name=_("Tier Name"))
    min_sales = models.IntegerField(verbose_name=_("Min Sales"))
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Commission Rate"))
    tier_benefits = models.TextField(blank=True, verbose_name=_("Tier Benefits"))
    access_level = models.IntegerField(verbose_name=_("Access Level"))
    next_tier_threshold = models.IntegerField(verbose_name=_("Next Tier Threshold"))
    tier_expiration = models.DateField(null=True, blank=True, verbose_name=_("Tier Expiration"))

    def __str__(self):
        return f"AffiliateTier {self.tier_name}"

    class Meta: 
        verbose_name = "Affiliate Tier"
        verbose_name_plural = "Affiliate Tiers"
