from rest_framework import serializers

from apps.users.models import VerificationCode


class PhoneAuthenticationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VerificationCode
        fields = ("phone",)
