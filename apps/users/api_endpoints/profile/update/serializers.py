from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "middle_name",
            "email",
            "photo",
            "job",
            "date_of_birth",
            "phone",
            "has_team",
            "team_size",
            "city",
        )
        extra_kwargs = {"phone": {"read_only": True}}
