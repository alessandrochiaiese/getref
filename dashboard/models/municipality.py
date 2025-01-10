from django.db import models

class Municipality(models.Model):
    #country = models.OneToOneField('Country', on_delete=models.CASCADE, related_name='region_country')
    region = models.ForeignKey('Region', on_delete=models.CASCADE, null=False, blank=False, related_name="municipality_region")
    province = models.ForeignKey('Province', on_delete=models.CASCADE, null=False, blank=False, related_name="municipality_province")
    name = models.CharField(max_length=64)
    is_capital_province = models.BooleanField(default=False)
    cadastral_code = models.CharField(max_length=4)
    latitude = models.FloatField(default=0.000000)
    longitude = models.FloatField(default=0.000000)

    class Meta:
        verbose_name = "Municipality"
        verbose_name_plural = "Municipalities" 