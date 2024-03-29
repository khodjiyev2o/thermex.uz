# Generated by Django 4.2 on 2023-05-11 12:13

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("common", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="VerificationCode",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Created at")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Updated at")),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=32, null=True, region=None, verbose_name="Phone number"
                    ),
                ),
                ("code", models.CharField(blank=True, max_length=10, verbose_name="Code")),
                ("expires_at", models.DateTimeField(blank=True, null=True, verbose_name="Expires In")),
            ],
            options={
                "verbose_name": "Verification Code",
                "verbose_name_plural": "Verification Codes",
                "ordering": ("-created_at",),
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Created at")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Updated at")),
                ("first_name", models.CharField(max_length=255, null=True, verbose_name="First Name")),
                ("last_name", models.CharField(max_length=255, null=True, verbose_name="Last Name")),
                ("middle_name", models.CharField(max_length=255, null=True, verbose_name="Middle Name")),
                ("username", models.CharField(max_length=255, null=True, unique=True, verbose_name="Username")),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=32, region=None, unique=True, verbose_name="Phone number"
                    ),
                ),
                ("email", models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name="Email")),
                ("photo", models.FileField(blank=True, null=True, upload_to="users/%Y/%m", verbose_name="Photo")),
                ("date_of_birth", models.DateField(blank=True, null=True, verbose_name="Data of Birth")),
                ("has_team", models.BooleanField(default=False, verbose_name="Has Team")),
                ("team_size", models.PositiveIntegerField(default=1, verbose_name="Team Size")),
                ("is_active", models.BooleanField(default=True, verbose_name="Is Active")),
                ("is_staff", models.BooleanField(default=False, verbose_name="Is Staff")),
                ("is_superuser", models.BooleanField(default=False, verbose_name="Is SuperUser")),
                (
                    "city",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="common.city",
                        verbose_name="City",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "job",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="common.occupation",
                        verbose_name="Occupation",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "User",
                "verbose_name_plural": "Users",
            },
        ),
    ]
