# referral_system/models.py

import email
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class Referral(models.Model):
    program = models.ForeignKey('ReferralProgram', on_delete=models.CASCADE, verbose_name=_("Program"), related_name="referrals", null=True, blank=True)
    referrer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Referrer"), related_name="referrals_made")
    referred = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Referred"), related_name="referrals_received") 
    reward_given = models.BooleanField(default=False, verbose_name=_("Reward Given"))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))

    def __str__(self):
        #if self.referred != None:
        #    return f"{self.referrer.username} referred {self.referred.username}"

        return f"Referral {self.program} {self.referrer} {self.referred}"
        return f"{self.referrer.username} have not yet invited anyone"
    
    class Meta: 
        verbose_name = "Referral"
        verbose_name_plural = "Referrals"
