from django.db import models


class ReferralBonus(models.Model):
    programs = models.ManyToManyField('ReferralProgram', related_name='referral_bonus_programs')
    bonus_type = models.CharField(max_length=50)
    bonus_value = models.DecimalField(max_digits=10, decimal_places=2)
    min_referrals_required = models.IntegerField(default=0)
    bonus_date = models.DateField()
    expiry_date = models.DateField(null=True, blank=True)
    max_usage = models.IntegerField(default=1)
    eligibility_criteria = models.TextField(blank=True)

    class Meta:
        ordering = ['-expiry_date']
        verbose_name = "Referral Bonus"
        verbose_name_plural = "Referral Bonus"
