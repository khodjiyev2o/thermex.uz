from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from apps.products.api_endpoints.sold_products.serializers import (
    CreateSoldProductSerializer,
    ListSoldProductSerializer,
    UserPointSerializer,
)
from apps.products.models import SoldProduct


class SoldProductCreatetView(CreateAPIView):
    queryset = SoldProduct.objects.all()
    serializer_class = CreateSoldProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserPointsView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserPointSerializer

    def get_object(self):
        return self.request.user


class UserSoldProductListView(ListAPIView):
    serializer_class = ListSoldProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SoldProduct.objects.filter(user=self.request.user)
