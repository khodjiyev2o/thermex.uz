from rest_framework.generics import GenericAPIView
from apps.users.api_endpoints.login.serializers import PhoneVerifySerializer
from rest_framework import status, response


class PhoneVerificationView(GenericAPIView):
    serializer_class = PhoneVerifySerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return response.Response({"success": True,
                                  "message": "Phone number verified successfully",
                                  "is_new": True if not user.first_name else False,
                                  "tokens": user.tokens},
                                 status=status.HTTP_201_CREATED)

