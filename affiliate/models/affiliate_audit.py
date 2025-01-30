from django.db import models
from django.utils.translation import gettext_lazy as _

class AffiliateAudit(models.Model):
    affiliates = models.ManyToManyField('Affiliate', blank=True, verbose_name=_("Affiliates"), related_name='affiliate_audit_affiliates') #[1,2]
    action_taken = models.TextField(verbose_name=_("Action Taken"))
    action_date = models.DateField(verbose_name=_("Action Date"))
    ip_address = models.GenericIPAddressField(verbose_name=_("IP Address"))
    device_info = models.TextField(verbose_name=_("Device Info"))
    location = models.CharField(max_length=100, verbose_name=_("Location"))
    
    class Meta:
        ordering = ['-action_date']
        verbose_name = "Affiliate Audit"
        verbose_name_plural = "Affiliate Audits"
