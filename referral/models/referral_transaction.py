from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from payments.models.order import Order

User = get_user_model()

class ReferralTransaction(models.Model):
    referral_code = models.ForeignKey('ReferralCode', on_delete=models.CASCADE, verbose_name=_("Referral Code"), related_name='referra_transaction_referral_code')
    referred_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("User"), related_name='referra_transaction_user')
    transaction_date = models.DateField(verbose_name=_("Transaction Date"))
    order = models.ForeignKey(Order, null=True, on_delete=models.CASCADE, verbose_name=_("Order"))
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Amount"))
    currency = models.CharField(max_length=10, verbose_name=_("Currency"))
    status = models.CharField(max_length=50, verbose_name=_("Status"))
    conversion_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Conversion Value"))
    discount_value = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, verbose_name=_("Discount Value"))
    coupon_code_used = models.CharField(max_length=100, blank=True, verbose_name=_("Coupon Code Used"))
    channel = models.CharField(max_length=50, blank=True, verbose_name=_("Channel"))

    def __str__(self):
        return f"Transaction {self.order}"
    
    class Meta:
        ordering = ['-transaction_date']
        verbose_name = "Referral Transaction"
        verbose_name_plural = "Referral Transactions"
