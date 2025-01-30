
from django.db import models
from django.utils.translation import gettext_lazy as _

from payments.models.product import Product

class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"), related_name='product')
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name=_("Price"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    def __str__(self) -> str:
        return f"{self.product.name} {self.price}"