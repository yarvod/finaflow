from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from api.views import health_check


schema_view = get_schema_view(
    openapi.Info(
        title="FinaFlow Backend API",
        default_version="v1",
        description="API endpoints described here",
        terms_of_service="",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    # path('jet/', include('jet.urls', 'jet')),
    re_path(
        r"^api-docs/swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^api-docs/swagger$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^api-docs/redoc$",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    path("admin/", admin.site.urls),
    path("api/", include(("api.urls", "api"))),
    url(r"^healthcheck$", health_check, name="health_check"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
