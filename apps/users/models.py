from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from apps.common.models import BaseModel
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=255, unique=True, null=True)
    phone = models.CharField(max_length=15, unique=True, null=True)
    email = models.EmailField(max_length=255, unique=True)
    photo = models.FileField(upload_to='users/%Y/%m', blank=True, null=True)
    is_creator = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # type: ignore

    def __str__(self):
        if self.email:
            return self.email
        if self.phone:
            return self.phone
        if self.username:
            return self.username
        return f"{self.id}, User without data"

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
