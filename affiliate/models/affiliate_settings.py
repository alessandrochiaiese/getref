from django.db import models
from django.utils.translation import gettext_lazy as _

class AffiliateSettings(models.Model):
    affiliates = models.ManyToManyField('Affiliate', verbose_name=_("Affiliates"), related_name='affiiate_setting_affiliates') 
    preferred_currency = models.CharField(max_length=10, verbose_name=_("Preferred Currency"))
    preferred_payment_method = models.CharField(max_length=50, verbose_name=_("Preferred Payment Method"))
    payout_schedule = models.CharField(max_length=50, verbose_name=_("Payout Schedule"))
    notification_preference = models.CharField(max_length=50, verbose_name=_("Notification Preference"))
    dashboard_layout = models.CharField(max_length=50, verbose_name=_("Dashboard Layout"))
    
    class Meta: 
        verbose_name = "Affiliate Setting"
        verbose_name_plural = "Affiliate Settings"
