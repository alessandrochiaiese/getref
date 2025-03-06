from django.db import models
from django.utils.translation import gettext_lazy as _

class ReferralStats(models.Model):
    referral_code = models.ForeignKey('ReferralCode', on_delete=models.CASCADE, verbose_name=_("Referral Code"), related_name='referra_stats_referral_code')
    period = models.CharField(max_length=50, verbose_name=_("Period"))  # ad esempio "mensile", "annuale"
    click_count = models.IntegerField(default=0, verbose_name=_("Click Count"))
    conversion_count = models.IntegerField(default=0, verbose_name=_("Conversion Count"))
    total_rewards = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Total Rewards"))
    average_conversion_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Average Conversione Value"))
    highest_referral_earning = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Highest Referral Earning"))

    def __str__(self):
        return f"Stats for {self.referral_code.code} in {self.period}"

    class Meta: 
        verbose_name = "Referral Stat"
        verbose_name_plural = "Referral Stats"
