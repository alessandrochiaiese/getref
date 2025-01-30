from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class ReferralEngagement(models.Model):
    referral_codes = models.ManyToManyField('ReferralCode', verbose_name=_("Referral Codes"), related_name='referral_engagement_referral_codes')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("User"), related_name='user')
    email_opened = models.BooleanField(default=False, verbose_name=_("Email Opened"))
    email_clicked = models.BooleanField(default=False, verbose_name=_("Email Clicked"))
    social_share_count = models.IntegerField(default=0, verbose_name=_("Social Share Count"))
    last_interaction_date = models.DateField(null=True, blank=True, verbose_name=_("Last Interaction Date"))
    
    class Meta:
        ordering = ['-last_interaction_date']
        verbose_name = "Referral Engagement"
        verbose_name_plural = "Referral Engagements"
