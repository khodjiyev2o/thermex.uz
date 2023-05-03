from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.urls import path

from .api_endpoints import auth

application_urlpatterns = [
    path(
        "send-phone-authentication-code/",
        auth.PhoneAuthenticationView.as_view(),
        name="send-phone-authentication-code",
    ),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

urlpatterns = application_urlpatterns
