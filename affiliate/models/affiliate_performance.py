from django.db import models
from django.utils.translation import gettext_lazy as _

PERIOD_CHOICES = [
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly'),
    ('annual', 'Annual'),
]

class AffiliatePerformance(models.Model):
    affiliates = models.ManyToManyField('Affiliate', verbose_name=_("Affiliates"), related_name='affiliate_performance_affiliates') 
    period = models.CharField(max_length=50, choices=PERIOD_CHOICES, verbose_name=_("Period"))
    total_clicks = models.IntegerField(verbose_name=_("Total Clicks"))
    total_conversions = models.IntegerField(verbose_name=_("Total Conversions"))
    conversion_rate = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Conversion Rate"))
    total_earnings = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Total Earnings"))
    average_order_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Average Order Value"))
    refund_rate = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Refund Rate"))
    customer_lifetime_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Customer Lifetime Value"))
    top_product = models.CharField(max_length=255, verbose_name=_("Top Product"))
    
    class Meta: 
        verbose_name = "Affiliate Perfomance"
        verbose_name_plural = "Affiliate Perfomances"
