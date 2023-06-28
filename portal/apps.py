from django.apps import AppConfig

from portal.settings import SITE_NAME


class PortalConfig(AppConfig):
    name = "portal"
    verbose_name = SITE_NAME
