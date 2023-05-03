from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from apps.common.models import BaseModel, Region
from .managers import UserManager
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    middle_name = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=255, unique=True, null=True)
    phone = PhoneNumberField(_("Phone number"), max_length=32, unique=True, null=True)
    email = models.EmailField(max_length=255, unique=True)
    photo = models.FileField(upload_to='users/%Y/%m', blank=True, null=True)
    has_team = models.BooleanField(default=False)
    team_size = models.PositiveIntegerField(default=1)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []  # type: ignore

    def __str__(self):
        if self.email:
            return self.email
        if self.phone:
            return self.phone
        if self.username:
            return self.username
        return f"{self.id}, User without data"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def tokens(self):
        token = RefreshToken.for_user(self)
        return {'access': str(token.access_token), 'refresh': str(token)}

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class VerificationCode(BaseModel):
    phone = PhoneNumberField(_("Phone number"), max_length=32, unique=True, null=True)
    code = models.CharField(max_length=10, blank=True, help_text="This field is created automatically")
    is_active = models.BooleanField(default=False, verbose_name="Is Active")
    expires_at = models.DateTimeField(verbose_name="Expires In", null=True, blank=True)

    class Meta:
        verbose_name = "Verification Code"
        verbose_name_plural = "Verification Code"

        def __str__(self):
            return f"User ID: {self.user.id} | User email: {self.code}"

    @property
    def is_expired(self):
        return self.expires_at <= timezone.now()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.expires_at = self.created_at + timezone.timedelta(minutes=5)
        return super().save(*args, **kwargs)
