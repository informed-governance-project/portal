from django.apps import AppConfig

from proxy.settings import SITE_NAME


class ProxyConfig(AppConfig):
    name = "proxy"
    verbose_name = SITE_NAME
