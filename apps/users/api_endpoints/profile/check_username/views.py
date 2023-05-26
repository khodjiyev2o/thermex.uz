from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from apps.users.api_endpoints.profile.check_username.serializers import (
    CheckUsernameSerializer,
)
from apps.users.models import User


class CheckUsernameView(GenericAPIView):
    serializer_class = CheckUsernameSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            username = request.data.get("username")
            self.queryset.get(username=username)
            raise ValidationError(detail={"username": _("Username is already taken")}, code="exists")
        except User.DoesNotExist:
            return Response({"success": True, "message": "Username is available"}, status=status.HTTP_200_OK)
