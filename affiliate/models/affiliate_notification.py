from django.db import models
from django.utils.translation import gettext_lazy as _

class AffiliateNotification(models.Model):
    affiliates = models.ManyToManyField('Affiliate', verbose_name=_("Affiliates"), related_name='affiliate_notification_affiliates') 
    message = models.TextField(verbose_name=_("Message"))
    date_sent = models.DateField(verbose_name=_("Date Sent"))
    is_read = models.BooleanField(default=False, verbose_name=_("Is Read"))
    priority = models.CharField(max_length=50, verbose_name=_("Priority"))
    notification_type = models.CharField(max_length=50, verbose_name=_("Notification Type"))

    class Meta:
        ordering = ['-date_sent']
        verbose_name = "Affiliate Notification"
        verbose_name_plural = "Affiliate Notifications"
