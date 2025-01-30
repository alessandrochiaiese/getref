# referral_system/models.py

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class ReferralReward(models.Model):
    referral_codes = models.ManyToManyField('ReferralCode', verbose_name=_("Referral Codes"), related_name='referra_reward_referral_codes')
    referred_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("User"), related_name='referra_reward_user')
    reward_type = models.CharField(max_length=50, verbose_name=_("Reward Type"))
    reward_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Reward Value"))
    date_awarded = models.DateField(verbose_name=_("Date Awarded"))
    status = models.CharField(max_length=50, verbose_name=_("Status"))
    expiry_date = models.DateField(null=True, blank=True, verbose_name=_("Expiry Date"))
    reward_description = models.TextField(blank=True, verbose_name=_("Reward Description"))
    reward_source = models.CharField(max_length=100, blank=True, verbose_name=_("Reward Source"))

    class Meta:
        ordering = ['-date_awarded']
        verbose_name = "Referral Reward"
        verbose_name_plural = "Referral Rewards"
