# Generated by Django 4.2 on 2023-05-18 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0002_alter_occupation_name_alter_occupation_name_ru_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Notification",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Created at")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Updated at")),
                ("title", models.CharField(max_length=255, verbose_name="Title")),
                ("text", models.TextField(verbose_name="Title")),
                ("image", models.ImageField(blank=True, null=True, upload_to="notifications/%Y/%m/")),
            ],
            options={
                "verbose_name": "Notification",
                "verbose_name_plural": "Notifications",
            },
        ),
    ]
