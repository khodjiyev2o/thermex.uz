
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from apps.common.models import Region
from apps.common.choices import City
from apps.common.serializers import RegionListSerializer, RegionDetailSerializer
from django.http import JsonResponse


class CityListView(APIView):

    def get(self, request):
        cities = list(City.choices)
        return JsonResponse({'cities': cities})


class RegionDetailView(ListAPIView):
    serializer_class = RegionDetailSerializer

    def get_queryset(self):
        city = self.kwargs.get('city')
        return Region.objects.filter(city=city)


class RegionListView(ListAPIView):
    serializer_class = RegionListSerializer
    queryset = Region.objects.all()
