from django.db import models
from django.utils.translation import gettext_lazy as _

from payments.models.order import Order
from payments.models.product import Product

class AffiliateTransaction(models.Model):
    commissions = models.ManyToManyField('AffiliateCommission', related_name='affiliate_transaction_commissions')
    affiliates = models.ManyToManyField('Affiliate', verbose_name=_("Affiliates"), related_name='affiliate_transaction_affiliates') 
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Transaction Amount"))
    transaction_date = models.DateField(verbose_name=_("Transaction Date"))
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name=_("Order"))
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"))
    status = models.CharField(max_length=50, verbose_name=_("Status"))
    payment_date = models.DateField(null=True, blank=True, verbose_name=_("Payment Date"))
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Commission Rate"))
    discount_applied = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, verbose_name=_("Discount Applied"))
    coupon_code = models.CharField(max_length=255, blank=True, verbose_name=_("Coupon Code"))

    class Meta: 
        verbose_name = "Affiliate Transaction"
        verbose_name_plural = "Affiliate Transactions"
