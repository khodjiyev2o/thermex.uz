# Generated by Django 4.2 on 2023-06-06 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalogue", "0002_prizechildcategory_name_ru_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="prizeproduct",
            name="description_ru",
            field=models.TextField(blank=True, null=True, verbose_name="Description"),
        ),
        migrations.AddField(
            model_name="prizeproduct",
            name="description_uz",
            field=models.TextField(blank=True, null=True, verbose_name="Description"),
        ),
        migrations.AlterField(
            model_name="prizechildcategory",
            name="name",
            field=models.CharField(max_length=256, verbose_name="Name"),
        ),
        migrations.AlterField(
            model_name="prizechildcategory",
            name="name_ru",
            field=models.CharField(max_length=256, null=True, verbose_name="Name"),
        ),
        migrations.AlterField(
            model_name="prizechildcategory",
            name="name_uz",
            field=models.CharField(max_length=256, null=True, verbose_name="Name"),
        ),
    ]
