
from locale import currency
from django.db import models
from django.utils.translation import gettext_lazy as _

from payments.models.product_tag import ProductTag
from payments.models.utils import get_image_filename
"""
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Prezzo con 2 decimali
    quantity_in_stock = models.IntegerField()  # Quantità disponibile in magazzino
    created_at = models.DateTimeField(auto_now=True)  # Data e ora di creazione dell'ordine
    
    def __str__(self):
        return self.name
"""
class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Name"))
    #tags = models.ManyToManyField(ProductTag, blank=True, related_name="tags")
    description = models.TextField(max_length=1000, blank=True, verbose_name=_("Description"))
    thumbnail = models.ImageField(upload_to=get_image_filename, blank=True, verbose_name=_("Thumbnail"))
    url = models.URLField(verbose_name=_("URL"))  
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, verbose_name=_("Price"))  # Prezzo con 2 decimali
    quantity = models.IntegerField(default=1, verbose_name=_("Quantity"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    class Meta:
        ordering = ("-created_at",)
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name
