from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.users.manager import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=128, verbose_name=_("First name"))
    last_name = models.CharField(max_length=128, verbose_name=_("Last name"))
    middle_name = models.CharField(
        max_length=128, blank=True, null=True, verbose_name=_("Middle name")
    )
    phone_number = models.CharField(
        max_length=20, blank=True, null=True, verbose_name=_("Phone number")
    )
    username = models.CharField(max_length=128, unique=True, verbose_name=_("Username"))
    email = models.EmailField(verbose_name=_("Email"))

    is_active = models.BooleanField(default=True, verbose_name=_("Is active"))
    is_staff = models.BooleanField(default=False, verbose_name=_("Is staff"))
    is_superuser = models.BooleanField(default=False, verbose_name=_("Is superuser"))

    REQUIRED_FIELDS = ["first_name", "last_name"]
    USERNAME_FIELD = "username"

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
