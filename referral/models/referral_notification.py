from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

class ReferralNotification(models.Model):
    NOTIFICATION_TYPE_CHOICES = [
        ('Bonus', 'Bonus'),
        ('Alert', 'Alert'),
        ('Reminder', 'Reminder'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("User"), related_name='engagement_notification_user')
    message = models.TextField(verbose_name=_("Message"))
    date_sent = models.DateField(verbose_name=_("Date Sent"))
    is_read = models.BooleanField(default=False, verbose_name=_("Is Read"))
    notification_type = models.CharField(max_length=50, choices=NOTIFICATION_TYPE_CHOICES, verbose_name=_("Notification Type"))
    priority = models.CharField(max_length=50, verbose_name=_("Priority"))
    action_required = models.BooleanField(default=False, verbose_name=_("Action Required"))

    def __str__(self):
        return f"Notification to {self.user.name}"

    class Meta:
        ordering = ['-date_sent']
        verbose_name = "Referral Notification"
        verbose_name_plural = "Referral Notifications"
