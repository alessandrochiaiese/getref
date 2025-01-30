from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

class ReferralCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("User"), related_name='referral_code_user')
    programs = models.ManyToManyField('ReferralProgram', verbose_name=_("Programs"), related_name='referral_code_programs')
    code = models.CharField(max_length=50, unique=True, verbose_name=_("Code"))
    usage_count = models.IntegerField(default=0, verbose_name=_("Usage Count"))
    date_created = models.DateField(auto_now_add=True, verbose_name=_("Date Created"))
    status = models.CharField(max_length=50, verbose_name=_("Status"))
    expiry_date = models.DateField(null=True, blank=True, verbose_name=_("Expiry Date"))
    referred_user_count = models.IntegerField(default=0, verbose_name=_("Referred User Count"))
    unique_url = models.URLField(blank=True, verbose_name=_("Unique URL"))
    campaign_source = models.CharField(max_length=100, blank=True, verbose_name=_("Campaign Source"))
    campaign_medium = models.CharField(max_length=100, blank=True, verbose_name=_("Campaign Medium"))

    class Meta:
        ordering = ['-date_created']
        verbose_name = "Referral Code"
        verbose_name_plural = "Referral Codes"
