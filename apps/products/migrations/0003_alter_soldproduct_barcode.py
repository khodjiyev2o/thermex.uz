# Generated by Django 4.2 on 2023-05-13 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_soldproduct_barcode_soldproduct_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soldproduct',
            name='barcode',
            field=models.CharField(max_length=15, unique=True, verbose_name='Bar Code'),
        ),
    ]
