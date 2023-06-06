from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework_simplejwt.tokens import RefreshToken

from apps.common.models import BaseModel, City, Occupation

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    first_name = models.CharField(_("First Name"), max_length=255)
    last_name = models.CharField(_("Last Name"), max_length=255, null=True)
    middle_name = models.CharField(_("Middle Name"), max_length=255, null=True)
    username = models.CharField(_("Username"), max_length=255, unique=True, null=True)
    phone = PhoneNumberField(_("Phone number"), max_length=32, unique=True)
    email = models.EmailField(_("Email"), max_length=255, null=True, blank=True)
    photo = models.ImageField(_("Photo"), upload_to="users/%Y/%m", blank=True, null=True)
    job = models.ForeignKey(Occupation, verbose_name=_("Occupation"), null=True, on_delete=models.CASCADE)
    date_of_birth = models.DateField(_("Data of Birth"), blank=True, null=True)
    has_team = models.BooleanField(_("Has Team"), default=False)
    team_size = models.PositiveIntegerField(_("Team Size"), default=1)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name=_("City"), null=True, blank=True)
    points = models.PositiveIntegerField(default=0, verbose_name=_("Points"))
    is_active = models.BooleanField(_("Is Active"), default=True)
    is_staff = models.BooleanField(_("Is Staff"), default=False)
    is_superuser = models.BooleanField(_("Is SuperUser"), default=False)

    objects = UserManager()
    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []  # type: ignore

    def __str__(self):
        if self.phone:
            return f"{self.phone}"
        if self.username:
            return self.username
        return f"{self.id}, User without data"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def tokens(self):
        token = RefreshToken.for_user(self)
        return {"access": str(token.access_token), "refresh": str(token)}

    @property
    def life_time_collected_points(self):
        return self.sold_products.aggregate(points=models.Sum("product__point"))["points"] or 0

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")


class VerificationCode(BaseModel):
    phone = PhoneNumberField(_("Phone number"), max_length=32, null=True)
    code = models.CharField(
        _("Code"),
        max_length=10,
        blank=True,
    )
    expires_at = models.DateTimeField(verbose_name=_("Expires In"), null=True, blank=True)

    class Meta:
        verbose_name = _("Verification Code")
        verbose_name_plural = _("Verification Codes")
        ordering = ("-created_at",)

        def __str__(self):
            return f"User ID: {self.user.id} | User email: {self.code}"

    @property
    def is_expired(self):
        return self.expires_at <= timezone.now()

    def save(self, *args, **kwargs):
        if not self.pk:
            self.expires_at = timezone.now() + timezone.timedelta(minutes=2)
        return super().save(*args, **kwargs)
