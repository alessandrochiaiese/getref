from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class AffiliateLink(models.Model):
    affiliates = models.ManyToManyField('Affiliate', verbose_name=_("Affiliates"), related_name='affiliate_link_affiliates')
    programs = models.ManyToManyField('AffiliateProgram', verbose_name=_("Programs"), related_name='affiliate_link_programs')
    url = models.URLField(verbose_name=_("URL"))
    click_count = models.IntegerField(default=0, verbose_name=_("Click Count"))
    conversion_count = models.IntegerField(default=0, verbose_name=_("Conversion Count"))
    date_created = models.DateField(verbose_name=_("Date Created"))
    last_used = models.DateTimeField(null=True, blank=True, verbose_name=_("Last Used"))
    link_status = models.CharField(max_length=50, verbose_name=_("Link Status"))
    landing_page = models.URLField(blank=True, verbose_name=_("Landing Page"))
    custom_tracking_id = models.CharField(max_length=255, blank=True, verbose_name=_("Custom Tracking ID"))

    def __str__(self):
        return f"Link by {self.url}"
    
    class Meta:
        ordering = ['-date_created']
        verbose_name = "Affiliate Link"
        verbose_name_plural = "Affiliate Links"
