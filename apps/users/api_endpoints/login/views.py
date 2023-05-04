from rest_framework.views import APIView
from apps.users.api_endpoints.login.serializers import PhoneAuthenticationSerializer
from rest_framework import status, response


class PhoneVerificationView(APIView):
    serializer_class = PhoneAuthenticationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return response.Response({"success": True,
                                  "message": "Phone number verified successfully",
                                  "id": user.id},
                                 status=status.HTTP_201_CREATED)


