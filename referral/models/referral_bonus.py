from django.db import models
from django.utils.translation import gettext_lazy as _

class ReferralBonus(models.Model):
    programs = models.ManyToManyField('ReferralProgram', verbose_name=_("Programs"), related_name='referral_bonus_programs')
    bonus_type = models.CharField(max_length=50, verbose_name=_("Bonus Type"))
    bonus_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Bonus Value"))
    min_referrals_required = models.IntegerField(default=0, verbose_name=_("Min Referrals Required"))
    bonus_date = models.DateField(verbose_name=_("Bonus Date"))
    expiry_date = models.DateField(null=True, blank=True, verbose_name=_("Expiry Date"))
    max_usage = models.IntegerField(default=1, verbose_name=_("Max Usage"))
    eligibility_criteria = models.TextField(blank=True, verbose_name=_("Eligibility Criteria"))

    class Meta:
        ordering = ['-expiry_date']
        verbose_name = "Referral Bonus"
        verbose_name_plural = "Referral Bonus"
