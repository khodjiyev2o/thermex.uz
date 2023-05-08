from rest_framework import serializers
from django.contrib.auth import get_user_model
from apps.common.serializers import RegionListSerializer
User = get_user_model()


class UpdateProfileSerializer(serializers.ModelSerializer):
    region = RegionListSerializer()

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
            'job',
            'date_of_birth',
            'phone',
            'has_team',
            'team_size',
            'region',
        )
        extra_kwargs = {"phone": {"read_only": True}}
