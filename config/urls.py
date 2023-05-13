from django.contrib import admin
from django.urls import path, include
from .swagger import swaggerurlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
    path("api/v1/users/", include("apps.users.urls")),
    path("api/v1/common/", include("apps.common.urls")),
    path("api/v1/products/", include("apps.products.urls")),
]
urlpatterns += i18n_patterns(path("admin/", admin.site.urls))
urlpatterns += swaggerurlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
