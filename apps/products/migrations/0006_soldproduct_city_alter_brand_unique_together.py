# Generated by Django 4.2 on 2023-05-14 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_alter_occupation_name_alter_occupation_name_ru_and_more'),
        ('products', '0005_alter_category_name_alter_category_name_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='soldproduct',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='common.city', verbose_name='City'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='brand',
            unique_together={('category', 'name')},
        ),
    ]
