from django.urls import path
from apps.social_auth.api_endpoints.views import GoogleLogin

urlpatterns = [
    path('google/', GoogleLogin.as_view(), name='google-social-login')
]
