from django.db import models
from django.utils.translation import gettext_lazy as _

class Municipality(models.Model):
    #country = models.OneToOneField('Country', on_delete=models.CASCADE, related_name='region_country')
    region = models.ForeignKey('Region', on_delete=models.CASCADE, null=False, blank=False, verbose_name=_("Region"), related_name="municipality_region")
    province = models.ForeignKey('Province', on_delete=models.CASCADE, null=False, blank=False, verbose_name=_("Province"), related_name="municipality_province")
    name = models.CharField(max_length=64, verbose_name=_("Name"))
    is_capital_province = models.BooleanField(default=False, verbose_name=_("Is Capital Province"))
    cadastral_code = models.CharField(max_length=4, verbose_name=_("Cadastral Code"))
    latitude = models.FloatField(default=0.000000, verbose_name=_("Latitude"))
    longitude = models.FloatField(default=0.000000, verbose_name=_("Longitude"))

    class Meta:
        verbose_name = "Municipality"
        verbose_name_plural = "Municipalities" 