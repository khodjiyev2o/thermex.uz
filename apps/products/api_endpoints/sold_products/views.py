from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from apps.products.models import SoldProduct
from apps.products.api_endpoints.sold_products.serializers import CreateSoldProductSerializer, ListSoldProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Sum


class SoldProductCreatetView(CreateAPIView):
    queryset = SoldProduct.objects.all()
    serializer_class = CreateSoldProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserPointsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        points = SoldProduct.objects.filter(user=self.request.user).aggregate(points=Sum('product__point'))['points']
        data = {
            "success": True,
            "message": "Successfull",
            "points": points or 0
        }
        return Response(data)


class UserSoldProductListView(ListAPIView):
    serializer_class = ListSoldProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SoldProduct.objects.filter(user=self.request.user)
