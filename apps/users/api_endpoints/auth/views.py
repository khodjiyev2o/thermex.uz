from rest_framework.generics import CreateAPIView
from apps.users.models import VerificationCode
from apps.users.api_endpoints.auth.serializers import PhoneAuthenticationSerializer
from rest_framework.response import Response
from apps.users.api_endpoints.auth.utils import send_activation_code_via_sms
import random
import string
from rest_framework import status
from django.utils import timezone


class PhoneAuthenticationView(CreateAPIView):
    queryset = VerificationCode
    serializer_class = PhoneAuthenticationSerializer
    code = "".join(random.choice(string.digits) for _ in range(4))

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone = serializer.validated_data.get("phone")
        try:
            VerificationCode.objects.get(phone=phone, expires_at__gt=timezone.now())
            return Response({"success": False, "message": "Activation code already sent !"})
        except VerificationCode.DoesNotExist:
            send_activation_code_via_sms(phone=phone, code=self.code)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({"success": True, "message": f"Activation code successfully sent to {phone}!"},
                            status=status.HTTP_201_CREATED,
                            headers=headers)
        except Exception as e:
            print(Exception)
            return Response({"success": False, "message": "Unexpected Error! "})

    def perform_create(self, serializer):
        serializer.save(code=self.code)
