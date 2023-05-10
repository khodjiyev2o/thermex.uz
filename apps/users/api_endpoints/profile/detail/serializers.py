from rest_framework import serializers
from django.contrib.auth import get_user_model
from apps.common.models import City
User = get_user_model()


class RegionListSerializer(serializers.ModelSerializer):
    region = serializers.CharField(source='region.name')

    class Meta:
        model = City
        fields = ('name', 'region')


class GetProfileDetailSerializer(serializers.ModelSerializer):
    city = RegionListSerializer()

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'middle_name',
            'email',
            'photo',
            'phone',
            'job',
            'date_of_birth',
            'has_team',
            'team_size',
            'city',
        )
