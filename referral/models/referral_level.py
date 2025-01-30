
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class ReferralLevel(models.Model): 
    referrer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Referrer"), related_name="referrals")
    referred = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Referred"), related_name="referred_by")  
    level = models.PositiveIntegerField(default=1, verbose_name=_("Level"))

