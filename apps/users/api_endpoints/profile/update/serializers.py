from rest_framework import serializers
from django.contrib.auth import get_user_model
from apps.common.serializers import RegionSerializer
User = get_user_model()


class UpdateProfileSerializer(serializers.ModelSerializer):
    region = RegionSerializer()

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
            'has_team',
            'team_size',
            'region',
        )
        extra_kwargs = {"phone": {"read_only": True}}
