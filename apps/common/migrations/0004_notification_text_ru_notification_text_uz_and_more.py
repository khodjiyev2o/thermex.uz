# Generated by Django 4.2 on 2023-05-18 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='notification',
            name='text_uz',
            field=models.TextField(null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='notification',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='notification',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Title'),
        ),
    ]