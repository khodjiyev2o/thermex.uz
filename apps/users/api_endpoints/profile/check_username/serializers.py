from django.contrib.auth.validators import UnicodeUsernameValidator
from rest_framework import serializers


class CheckUsernameSerializer(serializers.Serializer):
    username = serializers.CharField(validators=[UnicodeUsernameValidator()])
