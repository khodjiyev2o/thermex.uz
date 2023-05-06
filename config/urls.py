from django.contrib import admin
from django.urls import path, include
from .swagger import swaggerurlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/users/", include("apps.users.urls")),
    path("api/v1/common/", include("apps.common.urls")),
]
urlpatterns += swaggerurlpatterns
