from django.db import models
from django.utils.translation import gettext_lazy as _



class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


