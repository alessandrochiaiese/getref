from django.db import models
from django.utils.translation import gettext_lazy as _

class AffiliateSupportTicket(models.Model):
    affiliates = models.ManyToManyField('Affiliate', verbose_name=_("Affiliates"), related_name='affiliate_supportticket_affiliates') 
    ticket_number = models.CharField(max_length=100, verbose_name=_("Ticket Number"))
    subject = models.CharField(max_length=255, verbose_name=_("Subject"))
    description = models.TextField(verbose_name=_("Description"))
    status = models.CharField(max_length=50, verbose_name=_("Status"))
    date_created = models.DateField(verbose_name=_("Date Created"))
    date_closed = models.DateField(null=True, blank=True, verbose_name=_("Date Closed"))
    priority = models.CharField(max_length=50, verbose_name=_("Priority"))
    assigned_agent = models.CharField(max_length=255, verbose_name=_("Assigned Agent"))

    class Meta: 
        verbose_name = "Affiliate Support Ticket"
        verbose_name_plural = "Affiliate Support Tickets"
