from django.db import models

class Province(models.Model):
    #country = models.OneToOneField('Country', on_delete=models.CASCADE, related_name='region_country')
    region = models.ForeignKey('Region', on_delete=models.CASCADE, null=False, blank=False, related_name="province_region")
    metropolitan_city_code = models.CharField(max_length=5, null=True, blank=True)
    name = models.CharField(max_length=64)
    automotive_acronym = models.CharField(max_length=3)
    latitude = models.FloatField(default=0.000000)
    longitude = models.FloatField(default=0.000000)

    class Meta:
        verbose_name = "Province"
        verbose_name_plural = "Provinces" 