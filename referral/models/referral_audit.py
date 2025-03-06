from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

class ReferralAudit(models.Model):
    referral_code = models.ForeignKey('ReferralCode', on_delete=models.CASCADE, verbose_name=_("Referral Codes"), related_name='referral_audit_referral_code')
    action_taken = models.TextField(verbose_name=_("Action Taken"))
    action_date = models.DateField(verbose_name=_("Action Date"))
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("User"), related_name='referral_audit_referral_user')
    ip_address = models.GenericIPAddressField(verbose_name=_("IP Address"))
    device_info = models.TextField(verbose_name=_("Device Info"))
    location = models.CharField(max_length=100, verbose_name=_("Location"))


    class Meta:
        ordering = ['-action_date']
        verbose_name = "Referral Audit"
        verbose_name_plural = "Referral Audits"
