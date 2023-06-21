from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# define a token class for SSO on other application/module
class ExternalToken(models.Model):
    token = models.CharField(max_length=255)
    module_path = models.CharField(max_length=255)
    module_name = models.CharField(max_length=255)


# define an abstract class which make  the difference between operator and regulator
class User(AbstractUser):
    username = None
    is_regulator = models.BooleanField(default=False, verbose_name=_("Regulator"))
    is_staff = models.BooleanField(
        verbose_name=_("Administrator"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    phone_number = models.CharField(max_length=30, blank=True, default=None)
    email = models.EmailField(
        verbose_name=_("email address"),
        unique=True,
        error_messages={
            "unique": _("A user is already registered with this email address"),
        },
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
