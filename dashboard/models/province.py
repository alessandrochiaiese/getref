from django.db import models
from django.utils.translation import gettext_lazy as _

class Province(models.Model):
    #country = models.OneToOneField('Country', on_delete=models.CASCADE, related_name='region_country')
    region = models.ForeignKey('Region', on_delete=models.CASCADE, null=False, blank=False, verbose_name=_("Region"), related_name="province_region")
    metropolitan_city_code = models.CharField(max_length=5, null=True, blank=True, verbose_name=_("Metropolitan City Code"))
    name = models.CharField(max_length=64, verbose_name=_("Name"))
    automotive_acronym = models.CharField(max_length=3, verbose_name=_("Automotive Acronym"))
    latitude = models.FloatField(default=0.000000, verbose_name=_("Latitude"))
    longitude = models.FloatField(default=0.000000, verbose_name=_("Longitude"))

    class Meta:
        verbose_name = "Province"
        verbose_name_plural = "Provinces" 