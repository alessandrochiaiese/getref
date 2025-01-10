from django.db import models

class Region(models.Model):
    #country = models.OneToOneField('Country', on_delete=models.CASCADE, related_name='region_country')
    name = models.CharField(max_length=64)
    latitude = models.FloatField(default=0.000000)
    longitude = models.FloatField(default=0.000000)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions" 