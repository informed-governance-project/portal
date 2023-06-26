from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from .views import ExternalTokenApiView

urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="proxy"),
    path(
        "swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="proxy"),
        name="swagger-ui",
    ),
    path("redoc/", SpectacularRedocView.as_view(url_name="proxy"), name="redoc"),
    path("externaltoken/", ExternalTokenApiView.as_view()),
]
