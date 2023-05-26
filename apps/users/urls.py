from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .api_endpoints import auth, login, profile


application_urlpatterns = [
    path("phone-verify/", login.PhoneVerificationView.as_view(), name="phone-verify"),
    path("check-username/", profile.CheckUsernameView.as_view(), name="check-username"),
    path("profile/", profile.GetProfileDetailView.as_view(), name="profile-detail"),
    path("profile/update/", profile.UpdateProfileView.as_view(), name="profile-update"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "send-phone-authentication-code/",
        auth.PhoneAuthenticationView.as_view(),
        name="send-phone-authentication-code",
    ),
]

urlpatterns = application_urlpatterns
