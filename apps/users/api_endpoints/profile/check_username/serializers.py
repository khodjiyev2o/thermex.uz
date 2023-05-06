from rest_framework import serializers

from django.contrib.auth.validators import UnicodeUsernameValidator


class CheckUsernameSerializer(serializers.Serializer):
    username = serializers.CharField(validators=[UnicodeUsernameValidator()])
