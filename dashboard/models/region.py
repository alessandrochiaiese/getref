from django.db import models
from django.utils.translation import gettext_lazy as _

class Region(models.Model):
    #country = models.OneToOneField('Country', on_delete=models.CASCADE, related_name='region_country')
    name = models.CharField(max_length=64, verbose_name=_("Name"))
    latitude = models.FloatField(default=0.000000, verbose_name=_("Latitude"))
    longitude = models.FloatField(default=0.000000, verbose_name=_("Longitude"))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions" 