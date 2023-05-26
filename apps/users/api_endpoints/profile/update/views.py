from rest_framework import generics
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated

from apps.users.api_endpoints.profile.update.serializers import UpdateProfileSerializer


class UpdateProfileView(generics.UpdateAPIView):
    """
    Update profile information. Authentication is required!
    Send the data in  form-data format if you want to change the avatar.
    """

    serializer_class = UpdateProfileSerializer
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, JSONParser)

    def get_object(self):
        return self.request.user
