# referral_system/models.py

import email
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Referral(models.Model):
    program = models.OneToOneField('ReferralProgram', on_delete=models.CASCADE, related_name="referrals", null=True, blank=True)
    referrer = models.OneToOneField(User, on_delete=models.CASCADE, related_name="referrals_made")
    referred = models.ManyToManyField(User, related_name="referrals_received") 
    #referrer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="referrals")
    #referred = models.ForeignKey(User, on_delete=models.CASCADE, related_name="referred_by")  # non nullable
    reward_given = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        #if self.referred != None:
        #    return f"{self.referrer.username} referred {self.referred.username}"

        return f"{self.referrer.username} have not yet invited anyone"
    
    class Meta: 
        verbose_name = "Referral"
        verbose_name_plural = "Referrals"
