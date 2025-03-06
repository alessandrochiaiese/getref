# referral_system/models.py

from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from dashboard.models.region import Region

User = get_user_model()

class ReferralProgram(models.Model):
    REWARD_TYPE_CHOICES = [
        ('Cash', 'Cash'),
        ('Discount', 'Discount'),
        ('Points', 'Points'),
    ]
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"))
    reward_type = models.CharField(max_length=50, choices=REWARD_TYPE_CHOICES, verbose_name=_("Reward Type"))
    reward_value = models.DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name=_("Reward Value"))
    currency = models.CharField(max_length=10, verbose_name=_("Currency"))
    min_referral_count = models.IntegerField(default=0, verbose_name=_("Min Referral Count"))
    max_referrals_per_user = models.IntegerField(default=100, verbose_name=_("Max Referrals Per User"))
    date_created = models.DateField(auto_now_add=True, verbose_name=_("Date Created"))
    is_active = models.BooleanField(default=True, verbose_name=_("Is Active"))
    program_duration = models.IntegerField(default=90, verbose_name=_("Program Duration"))
    allowed_regions = models.ManyToManyField(Region, verbose_name=_("Allowed Regions"), related_name='engagement_program_regions')
    target_industry = models.CharField(max_length=100, verbose_name=_("Target Industry"))

    def __str__(self):
        return f"ReferralProgram {self.name}"
    
    class Meta:
        ordering = ['-date_created']
        verbose_name = "Referral Program"
        verbose_name_plural = "Referral Program"
