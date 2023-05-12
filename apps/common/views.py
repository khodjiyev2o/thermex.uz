
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from apps.common.models import Region, Occupation
from apps.common.choices import REGION_CHOICES
from apps.common.serializers import RegionListSerializer, OccupationListSerializer
from django.http import JsonResponse


class RegionNamesListView(APIView):

    def get(self, request):
        cities = list(REGION_CHOICES.keys())
        return JsonResponse({'cities': cities})


class RegionListView(ListAPIView):
    serializer_class = RegionListSerializer
    queryset = Region.objects.all()


class OccupationListView(ListAPIView):
    serializer_class = OccupationListSerializer
    queryset = Occupation.objects.all()
