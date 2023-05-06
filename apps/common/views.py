
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from apps.common.models import Region
from apps.common.choices import City
from apps.common.serializers import RegionListSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse


class CityListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cities = list(City.choices)
        return JsonResponse({'cities': cities})


class RegionListView(ListAPIView):
    serializer_class = RegionListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        city = self.kwargs.get('city')
        return Region.objects.filter(city=city)
