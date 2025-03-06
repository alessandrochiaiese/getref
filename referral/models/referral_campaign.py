from django.db import models
from django.utils.translation import gettext_lazy as _

class ReferralCampaign(models.Model):
    program = models.ForeignKey('ReferralProgram', on_delete=models.CASCADE, verbose_name=_("Program"), related_name='referral_campaign_program')
    campaign_name = models.CharField(max_length=255, verbose_name=_("Campaign Name"))
    start_date = models.DateField(verbose_name=_("Start Date"))
    end_date = models.DateField(verbose_name=_("End Date"))
    goal = models.TextField(verbose_name=_("Goal"))
    budget = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Budget"))
    spending_to_date = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Spending To Date"))
    target_audience = models.TextField(blank=True, verbose_name=_("Target Audience"))

    def __str__(self):
        return f"ReferralCampaign {self.campaign_name}"

    class Meta:
        ordering = ['-end_date']
        verbose_name = "Referral Campaign"
        verbose_name_plural = "Referral Campaigns"
