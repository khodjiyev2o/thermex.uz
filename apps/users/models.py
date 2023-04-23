from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from apps.common.models import BaseModel


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    pass