
from django.db import models
from django.utils.translation import gettext_lazy as _

class ProductTag(models.Model):
    name = models.CharField(
        max_length=100, help_text=_("Designates the name of the tag."),
        verbose_name=_("Name")
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ("-created_at",)
        db_table = 'product_tags'
        verbose_name = 'ProductTag'
        verbose_name_plural = 'ProductTags'
