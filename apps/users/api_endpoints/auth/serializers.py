from apps.users.models import VerificationCode
from rest_framework import serializers


class PhoneAuthenticationSerializer(serializers.ModelSerializer):

    class Meta:
        model = VerificationCode
        fields = ('phone', )
