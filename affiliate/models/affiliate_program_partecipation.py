from django.db import models
from django.utils.translation import gettext_lazy as _

class AffiliateProgramPartecipation(models.Model):
    affiliate = models.OneToOneField('Affiliate', on_delete=models.CASCADE, verbose_name=_("Affiliate"), related_name='affiliate_program_partecipation_affiliate')
    program = models.OneToOneField('AffiliateProgram', on_delete=models.CASCADE, verbose_name=_("Program"), related_name='affiliate_program_partecipation_program')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Joined"))
    commission_earned = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name=_("Commission Earned"))
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("inactive", "Inactive")], verbose_name=_("Status"))

    class Meta:
        ordering = ['-date_joined']
        verbose_name = "Affiliate Program Partecipation"
        verbose_name_plural = "Affiliate Program Partecipations"
