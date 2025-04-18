from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel
from apps.payment.choice import ProviderChoice, TransactionStatus
from apps.product.models import Product
from apps.users.models import User


class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("user"))
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("amount"))
    products = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("products"))

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        db_table = _("Orders")


class Providers(BaseModel):
    provider = models.CharField(choices=ProviderChoice.choices, max_length=65)
    key = models.CharField(max_length=255)
    key_description = models.TextField()
    value = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ("provider", "key")
        verbose_name = "Provider"
        verbose_name_plural = "Providers"


class Transaction(BaseModel):
    status = models.CharField(choices=TransactionStatus.choices, default=TransactionStatus.PENDING,
                              verbose_name=_("status"))
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name=_("order"))
    remote_id = models.CharField(_('Remote id'), max_length=255, null=True, blank=True)
    paid_at = models.DateTimeField(verbose_name=_("Paid at"), null=True, blank=True)
    canceled_at = models.DateTimeField(verbose_name=_("Canceled at"), null=True, blank=True)
    extra = models.JSONField(_('Extra'), null=True, blank=True)
    is_paid_with_card = models.BooleanField(default=False, verbose_name=_("Is paid with card ?"))
    provider = models.CharField(choices=ProviderChoice.choices, max_length=65)

    class Meta:
        db_table = 'Transaction'
        verbose_name = _('Transaction')
        verbose_name_plural = _('Transactions')
        ordering = ('remote_id',)

    def payment_url(self):
        payment_link = None

