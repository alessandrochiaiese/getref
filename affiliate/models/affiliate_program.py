from django.db import models
from django.utils.translation import gettext_lazy as _
from dashboard.models.region import Region 

class AffiliateProgram(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"))
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Commission Rate"))
    currency = models.CharField(max_length=10, verbose_name=_("Currency"))
    min_payout_threshold = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Min Payout Threshould"))
    max_payout_limit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Min Payout Limit"))
    date_created = models.DateField(verbose_name=_("Date Created"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))
    duration = models.IntegerField(verbose_name=_("Duration"))  # durata in giorni
    allowed_regions = models.ManyToManyField(Region, verbose_name=_("Allowed Regions"), related_name='affiliate_program_countries')
    target_industry = models.CharField(max_length=100, verbose_name=_("Target Industry"))

    class Meta:
        ordering = ['-date_created']
        verbose_name = "Affiliate Program"
        verbose_name_plural = "Affiliate Programs"
