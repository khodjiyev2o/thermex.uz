from apps.users.models import User, VerificationCode
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class PhoneVerifySerializer(serializers.Serializer):
    code = serializers.CharField()
    phone = PhoneNumberField(region="UZ")

    def validate_code(self, value):
        phone = self.initial_data.get('phone')
        obj = VerificationCode.objects.filter(phone=phone, code=value).order_by('-created_at').first()
        if obj is None or obj.is_expired is True:
            raise serializers.ValidationError(_('Invalid code'))
        if not obj.is_expired:
            return value

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation

    def create(self, validated_data):
        phone = validated_data.pop('phone')
        validated_data.pop('code', None)
        user, _ = User.objects.get_or_create(phone=phone)
        return user
