from django.db import models
from django.utils.translation import gettext_lazy as _

class ReferralCampaign(models.Model):
    programs = models.ManyToManyField('ReferralProgram', verbose_name=_("Programs"), related_name='referral_campaign_programs')
    campaign_name = models.CharField(max_length=255, verbose_name=_("Campaign Name"))
    start_date = models.DateField(verbose_name=_("Start Date"))
    end_date = models.DateField(verbose_name=_("End Date"))
    goal = models.TextField(verbose_name=_("Goal"))
    budget = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Budget"))
    spending_to_date = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Spending To Date"))
    target_audience = models.TextField(blank=True, verbose_name=_("Target Audience"))

    class Meta:
        ordering = ['-end_date']
        verbose_name = "Referral Campaign"
        verbose_name_plural = "Referral Campaigns"
