from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from referral.utils import default_expiry_date

User = get_user_model()

class ReferralCode(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Expired', 'Expired'),
        ('Used', 'Used'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("User"), related_name='referral_code_user')
    program = models.ForeignKey('ReferralProgram', null=True, blank=True, on_delete=models.CASCADE, verbose_name=_("Program"), related_name='referral_code_program')
    code = models.CharField(max_length=50, unique=True, verbose_name=_("Code"))
    usage_count = models.IntegerField(default=0, verbose_name=_("Usage Count"))
    date_created = models.DateField(auto_now_add=True, verbose_name=_("Date Created"))
    status = models.CharField(default='Active', max_length=50, choices=STATUS_CHOICES, verbose_name=_("Status"))
    expiry_date = models.DateField(default=default_expiry_date(), null=True, blank=True, verbose_name=_("Expiry Date"))
    referred_user_count = models.IntegerField(default=0, verbose_name=_("Referred User Count"))
    unique_url = models.URLField(blank=True, verbose_name=_("Unique URL"))
    campaign_source = models.CharField(max_length=100, blank=True, verbose_name=_("Campaign Source"))
    campaign_medium = models.CharField(max_length=100, blank=True, verbose_name=_("Campaign Medium"))

    def __str__(self):
        return f"ReferralCode {self.code}"
    
    class Meta:
        ordering = ['-date_created']
        verbose_name = "Referral Code"
        verbose_name_plural = "Referral Codes"
