import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _

from referral.utils import default_expiry_date

class ReferralBonus(models.Model):
    BONUS_TYPE_CHOICES = [
        ('Cash', 'Cash'),
        ('Discount', 'Discount'),
        ('Points', 'Points'),
    ]
    program = models.ForeignKey('ReferralProgram', on_delete=models.CASCADE, verbose_name=_("Program"), related_name='referral_bonus_program')
    bonus_type = models.CharField(default='Cash', max_length=50, choices=BONUS_TYPE_CHOICES, verbose_name=_("Bonus Type"))
    bonus_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Bonus Value"))
    min_referrals_required = models.IntegerField(default=0, verbose_name=_("Min Referrals Required"))
    bonus_date = models.DateField(auto_now_add=True, verbose_name=_("Bonus Date"))
    expiry_date = models.DateField(default=default_expiry_date(), null=True, blank=True, verbose_name=_("Expiry Date"))
    max_usage = models.IntegerField(default=1, verbose_name=_("Max Usage"))
    eligibility_criteria = models.TextField(blank=True, verbose_name=_("Eligibility Criteria"))

    def __str__(self):
        return f"ReferralBonus {self.program.name}"

    class Meta:
        ordering = ['-expiry_date']
        verbose_name = "Referral Bonus"
        verbose_name_plural = "Referral Bonus"
