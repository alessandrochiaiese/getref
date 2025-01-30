from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class AffiliateReward(models.Model):
    affiliate = models.OneToOneField('Affiliate', on_delete=models.CASCADE, verbose_name=_("Affiliate"), related_name="affiliate_reward_affiliates")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Amount"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))

    def __str__(self):
        return f"Reward for {self.amount} EUR"

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Affiliate Reward"
        verbose_name_plural = "Affiliate Rewards"
