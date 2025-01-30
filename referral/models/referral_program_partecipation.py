from django.db import models
from django.utils.translation import gettext_lazy as _

class ReferralProgramPartecipation(models.Model):
    referral_codes = models.OneToOneField('ReferralCode', on_delete=models.CASCADE, verbose_name=_("Referral Codes"), related_name='engagement_program_partecipation_referral_codes')
    programs = models.OneToOneField('ReferralProgram', on_delete=models.CASCADE, verbose_name=_("Programs"), related_name='engagement_program_partecipation_programs')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Joined"))
    reward_earned = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name=_("Reward Earned"))
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("inactive", "Inactive")], verbose_name=_("Status"))

    class Meta:
        ordering = ['-date_joined']
        verbose_name = "Referral Program Partecipation"
        verbose_name_plural = "Referral Program Partecipations"
