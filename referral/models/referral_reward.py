# referral_system/models.py

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from referral.utils import default_expiry_date

User = get_user_model()


class ReferralReward(models.Model):
    REWARD_TYPE_CHOICES = [
        ('Cash', 'Cash'),
        ('Discount', 'Discount'),
        ('Points', 'Points'),
    ]
    referral_code = models.ForeignKey('ReferralCode', on_delete=models.CASCADE, verbose_name=_("Referral Code"), related_name='referra_reward_referral_code')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("User"), related_name='referra_reward_user')
    reward_type = models.CharField(default='Cash', max_length=50, choices=REWARD_TYPE_CHOICES, verbose_name=_("Reward Type"))
    reward_value = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name=_("Reward Value"))
    date_awarded = models.DateField(auto_now_add=True, verbose_name=_("Date Awarded"))
    status = models.CharField(max_length=50, verbose_name=_("Status"))
    expiry_date = models.DateField(default=default_expiry_date(), null=True, blank=True, verbose_name=_("Expiry Date"))
    reward_description = models.TextField(blank=True, verbose_name=_("Reward Description"))
    reward_source = models.CharField(max_length=100, blank=True, verbose_name=_("Reward Source"))

    def __str__(self):
        return f"ReferralReward for {self.user.username}"

    class Meta:
        ordering = ['-date_awarded']
        verbose_name = "Referral Reward"
        verbose_name_plural = "Referral Rewards"
