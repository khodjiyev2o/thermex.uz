from rest_framework import serializers
from django.contrib.auth import get_user_model
from apps.users.api_endpoints.profile.detail.serializers import UserRegionListSerializer
User = get_user_model()


class UpdateProfileSerializer(serializers.ModelSerializer):
    city = UserRegionListSerializer()

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
            'city',
        )
        extra_kwargs = {"phone": {"read_only": True}}
