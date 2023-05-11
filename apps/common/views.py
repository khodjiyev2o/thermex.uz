
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from apps.common.models import Region
from apps.common.choices import REGION_CHOICES
from apps.common.serializers import RegionListSerializer
from django.http import JsonResponse
from django.utils import translation


class RegionNamesListView(APIView):

    def get(self, request):
        cities = list(REGION_CHOICES.keys())
        return JsonResponse({'cities': cities})


class RegionListView(ListAPIView):
    serializer_class = RegionListSerializer

    def get_queryset(self):
        queryset = Region.objects.all()
        if 'HTTP_ACCEPT_LANGUAGE' in self.request.META:
            lang = self.request.META['HTTP_ACCEPT_LANGUAGE']
            translation.activate(lang)
        return queryset
