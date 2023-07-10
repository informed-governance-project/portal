from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from .views import (
    ExternalTokenApiElemView,
    ExternalTokenApiView,
    ModuleApiView,
    UserApiView,
)

urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="portal"),
    path(
        "swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="portal"),
        name="swagger-ui",
    ),
    path("redoc/", SpectacularRedocView.as_view(url_name="portal"), name="redoc"),
    path("user/", UserApiView.as_view()),
    path("externaltoken/", ExternalTokenApiView.as_view()),
    path("externaltoken/<int:id>", ExternalTokenApiElemView.as_view()),
    path("module/", ModuleApiView.as_view()),
]
