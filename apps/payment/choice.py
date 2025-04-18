from django.db import models
from django.utils.translation import gettext_lazy as _


class ProviderChoice(models.TextChoices):
    PAYME = 'payme', "Paylov",
    PAYLOV = 'paylov', "Paylov",
    CLICK = 'click', 'CLICK'


class TransactionStatus(models.TextChoices):
    FAILED = _('failed'), _('Failed'),
    SUCCESS = _('success'), _('Success')
    PENDING = _('pending'), _('Pending')

