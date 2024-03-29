# Generated by Django 4.2 on 2023-06-06 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PrizeParentCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "name",
                    models.CharField(max_length=256, unique=True, verbose_name="Name"),
                ),
            ],
            options={
                "verbose_name": "PrizeParentCategory",
                "verbose_name_plural": "PrizeParentCategories",
            },
        ),
        migrations.CreateModel(
            name="PrizeChildCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "name",
                    models.CharField(max_length=256, verbose_name="PrizeChildCategory"),
                ),
                (
                    "parent_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalogue.prizeparentcategory",
                        verbose_name="PrizeParentCategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "PrizeChildCategory",
                "verbose_name_plural": "PrizeChildCategory",
                "unique_together": {("parent_category", "name")},
            },
        ),
        migrations.CreateModel(
            name="PrizeProduct",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                ("name", models.CharField(max_length=256, verbose_name="Name")),
                (
                    "sell_point",
                    models.PositiveIntegerField(default=100, verbose_name="Sell Point"),
                ),
                (
                    "photo",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="products/prize/%Y/%m",
                        verbose_name="Photo",
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalogue.prizechildcategory",
                        verbose_name="Category",
                    ),
                ),
            ],
            options={
                "verbose_name": "PrizeProduct",
                "verbose_name_plural": "PrizeProducts",
                "unique_together": {("name", "category")},
            },
        ),
    ]
