from django.db import models
from django.utils.translation import gettext_lazy as _

class ReferralProgramPartecipation(models.Model):
    STATUS_TYPE_CHOICES = [
        ("active", "Active"), 
        ("inactive", "Inactive")
    ]
    referral_code = models.ForeignKey('ReferralCode', on_delete=models.CASCADE, verbose_name=_("Referral Code"), related_name='engagement_program_partecipation_referral_code')
    program = models.ForeignKey('ReferralProgram', on_delete=models.CASCADE, verbose_name=_("Program"), related_name='engagement_program_partecipation_program')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Joined"))
    reward_earned = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name=_("Reward Earned"))
    status = models.CharField(max_length=50, choices=STATUS_TYPE_CHOICES, verbose_name=_("Status"))

    def __str__(self):
        return f"ReferralParticipation {self.id}"

    class Meta:
        ordering = ['-date_joined']
        verbose_name = "Referral Program Partecipation"
        verbose_name_plural = "Referral Program Partecipations"
