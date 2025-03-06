from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class ReferralSettings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("User"), related_name='referra_setting_user')
    default_reward_type = models.CharField(max_length=50, verbose_name=_("Default Reward Type"))
    max_referrals_allowed = models.IntegerField(default=100, verbose_name=_("Max Referrals Allowed"))
    notification_preference = models.CharField(max_length=50, verbose_name=_("Notification Preference"))
    auto_share_setting = models.BooleanField(default=True, verbose_name=_("Auto Share Setting"))
    social_share_message = models.TextField(blank=True, verbose_name=_("Social Share Message"))

    def __str__(self):
        return f"ReferralSettings for {self.user.name}"

    class Meta: 
        verbose_name = "Referral Settings"
        verbose_name_plural = "Referral Settings"
