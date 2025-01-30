from django.db import models
from django.utils.translation import gettext_lazy as _

class AffiliateCampaign(models.Model):
    programs = models.ManyToManyField('AffiliateProgram', verbose_name=_("Programs"), related_name='affiliate_campaign_programs')
    campaign_name = models.CharField(max_length=255, verbose_name=_("Campaign Name"))
    start_date = models.DateField(verbose_name=_("Start Date"))
    end_date = models.DateField(verbose_name=_("End Date"))
    goal = models.TextField(verbose_name=_("Goal"))
    budget = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Budget"))
    spending_to_date = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Spending To Date"))
    
    class Meta:
        ordering = ['-start_date']
        verbose_name = "Affiliate Campaign"
        verbose_name_plural = "Affiliate Campaigns"
