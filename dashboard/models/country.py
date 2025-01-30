from django.db import models
from django.utils.translation import gettext_lazy as _

class Country(models.Model):
    name = models.CharField(max_length=256, default="Italia", verbose_name=_("Name"))

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries" 