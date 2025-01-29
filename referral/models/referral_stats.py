from django.db import models


class ReferralStats(models.Model):
    referral_codes = models.ManyToManyField('ReferralCode', related_name='referra_stats_referral_codes')
    period = models.CharField(max_length=50)  # ad esempio "mensile", "annuale"
    click_count = models.IntegerField(default=0)
    conversion_count = models.IntegerField(default=0)
    total_rewards = models.DecimalField(max_digits=10, decimal_places=2)
    average_conversion_value = models.DecimalField(max_digits=10, decimal_places=2)
    highest_referral_earning = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta: 
        verbose_name = "Referral Stat"
        verbose_name_plural = "Referral Stats"
