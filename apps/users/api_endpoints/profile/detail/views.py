from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.users.api_endpoints.profile.detail.serializers import GetProfileDetailSerializer


class GetProfileDetailView(generics.RetrieveAPIView):
    """
    Get profile information. Authentication is required!
    """
    permission_classes = [IsAuthenticated]
    serializer_class = GetProfileDetailSerializer

    def get_object(self):
        return self.request.user
