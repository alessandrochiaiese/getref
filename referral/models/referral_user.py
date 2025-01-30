from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

class ReferralUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("user"), related_name='referra_user_user')
    total_referrals = models.IntegerField(default=0, verbose_name=_("Total Referrals"))
    active_referrals = models.IntegerField(default=0, verbose_name=_("Active Referrals"))
    inactive_referrals = models.IntegerField(default=0, verbose_name=_("Inactive Referrals"))
    total_rewards_earned = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Total Rewards Earned"))
    total_spent_by_referred_users = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Total Spent By Referred Users"))
    average_order_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Average Order Value"))
    loyalty_points_earned = models.IntegerField(default=0, verbose_name=_("Loyalty Points Earned"))

    class Meta: 
        verbose_name = "Referral User"
        verbose_name_plural = "Referral Users"
