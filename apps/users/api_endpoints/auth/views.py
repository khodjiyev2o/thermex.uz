from django.utils import timezone
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from apps.users.api_endpoints.auth.serializers import PhoneAuthenticationSerializer
from apps.users.api_endpoints.auth.utils import send_activation_code_via_sms
from apps.users.models import VerificationCode

from .utils import generate_code


class PhoneAuthenticationView(CreateAPIView):
    queryset = VerificationCode
    serializer_class = PhoneAuthenticationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data.get("phone")
        try:
            VerificationCode.objects.get(phone=phone, expires_at__gt=timezone.now())
            return Response({"success": False, "message": "Activation code already sent !"})
        except VerificationCode.DoesNotExist:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                {"success": True, "message": f"Activation code successfully sent to {phone}!"},
                status=status.HTTP_201_CREATED,
                headers=headers,
            )
        except Exception:
            return Response({"success": False, "message": "Unexpected Error! "})

    def perform_create(self, serializer):
        code = generate_code()
        send_activation_code_via_sms(phone=serializer.validated_data.get("phone"), code=code)
        serializer.save(code=code)
