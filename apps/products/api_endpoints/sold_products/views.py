from rest_framework.generics import CreateAPIView
from apps.products.models import SoldProduct
from apps.products.api_endpoints.sold_products.serializers import CreateSoldProductSerializer
from rest_framework.permissions import IsAuthenticated


class SoldProductCreatetView(CreateAPIView):
    queryset = SoldProduct.objects.all()
    serializer_class = CreateSoldProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
