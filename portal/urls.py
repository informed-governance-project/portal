"""
URL configuration for portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.decorators import login_required
from django.urls import include, path, re_path
from django.views.i18n import set_language
from revproxy.views import ProxyView
from two_factor.urls import urlpatterns as tf_urls
from two_factor.views import LoginView

from portal import views
from portal.admin import admin_site

# from portal.decorators import operateur_required, regulator_required
from portal.settings import CLIENT_REDIRECTIONS, DEBUG, REGULATOR_CONTACT, SITE_NAME
from proxy.views import DefaultProxyView

urlpatterns = [
    # Root
    path("", views.index, name="index"),
    # Admin
    path("admin/", admin_site.urls),
    # Accounts
    path("account/", include("django.contrib.auth.urls")),
    path("", include(tf_urls)),
    path(
        "account/login",
        LoginView.as_view(
            extra_context={"site_name": SITE_NAME, "regulator": REGULATOR_CONTACT},
            template_name="registration/login.html",
        ),
        name="login",
    ),
    # Logout
    path("logout", views.logout_view, name="logout"),
    # Terms of Service
    path("terms/", views.terms, name="terms"),
    # Privacy Policy
    path("privacy/", views.privacy, name="privacy"),
    # Language Selector
    path("set-language/", set_language, name="set_language"),
    # API
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/", include("proxy.api.urls")),
    #
    # Proxy views
    #
    re_path(
        r"^notifications/(?P<path>.*)$",
        ProxyView.as_view(upstream="http://127.0.0.1:5002/"),
    ),
]

# Proxy views as defined in CLIENT_REDIRECTIONS
for client in CLIENT_REDIRECTIONS:
    urlpatterns.append(
        re_path(
            client[0],
            login_required(
                DefaultProxyView.as_view(upstream=client[1]),
                login_url="/account/login",
            ),
        ),
    )

if DEBUG:
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
