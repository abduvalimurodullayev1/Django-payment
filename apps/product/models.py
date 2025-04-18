from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_("name"))
    description = models.TextField(verbose_name=_("description"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("price"))
    image = models.ImageField(upload_to='products/', verbose_name=_("image"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        db_table = _("Products")
