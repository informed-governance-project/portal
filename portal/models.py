from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from portal.helpers import generate_token


# define an abstract class which make the difference between operator and regulator
class User(AbstractUser):
    # username = None
    is_regulator = models.BooleanField(default=False, verbose_name=_("Regulator"))
    is_staff = models.BooleanField(
        verbose_name=_("Administrator"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    phone_number = models.CharField(max_length=30, blank=True, default=None, null=True)
    email = models.EmailField(
        verbose_name=_("email address"),
        unique=True,
        error_messages={
            "unique": _("A user is already registered with this email address"),
        },
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]


class Module(models.Model):
    """Proxified module of the SERIMA platform."""

    name = models.CharField(max_length=255, unique=True)
    path = models.CharField(max_length=255, unique=True)
    upstream = models.CharField(max_length=255, unique=True)
    authentication_required = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ExternalToken(models.Model):
    """Token class for SSO to other application/module of the SERIMA platform."""

    token = models.CharField(
        max_length=255, unique=True, null=False, default=generate_token
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
