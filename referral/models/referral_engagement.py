from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class ReferralEngagement(models.Model):
    referral_code = models.ForeignKey('ReferralCode', on_delete=models.CASCADE, verbose_name=_("Referral Code"), related_name='referral_engagement_referral_code')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("User"), related_name='user')
    email_opened = models.BooleanField(default=False, verbose_name=_("Email Opened"))
    email_clicked = models.BooleanField(default=False, verbose_name=_("Email Clicked"))
    social_share_count = models.IntegerField(default=0, verbose_name=_("Social Share Count"))
    last_interaction_date = models.DateField(null=True, blank=True, verbose_name=_("Last Interaction Date"))
    
    def __str__(self):
        return f"Engagement {self.referral_code} {self.user}"
    
    class Meta:
        ordering = ['-last_interaction_date']
        verbose_name = "Referral Engagement"
        verbose_name_plural = "Referral Engagements"
