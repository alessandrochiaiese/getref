from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

class ReferralConversion(models.Model):
    referral_codes = models.ManyToManyField('ReferralCode', verbose_name=_("Referral Codes"), related_name='referral_conversion_referral_codes')
    referred_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("User"), related_name='referral_conversion_user')
    conversion_date = models.DateField(verbose_name=_("Conversion Date"))
    conversion_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Conversion Value"))
    status = models.CharField(max_length=50, verbose_name=_("Status"))
    reward_issued = models.BooleanField(default=False, verbose_name=_("Reward Issued"))
    conversion_source = models.CharField(max_length=50, verbose_name=_("Conversion Source"))
    referral_type = models.CharField(max_length=50, blank=True, verbose_name=_("Referral Type"))

    class Meta:
        ordering = ['-conversion_date']
        verbose_name = "Referral Conversation"
        verbose_name_plural = "Referral Conversations"
