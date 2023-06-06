from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from apps.catalogue.api_endpoints.purchase_prize.serializers import PurchaseProductSerializer
from apps.products.models import UserBoughtProduct
from rest_framework import status
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _


class UserPurchasePrizeProductView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PurchaseProductSerializer
    queryset = UserBoughtProduct.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        thermex_product = serializer.validated_data.get("thermex_product", None)
        prize_product = serializer.validated_data.get("prize_product", None)

        product = thermex_product or prize_product

        if not self.has_enough_points(user=request.user, product=product):
            return Response({"detail": _("Not Enough points!")}, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @staticmethod
    def has_enough_points(user, product):
        if user.points < product.sell_point:
            return False
        return True
