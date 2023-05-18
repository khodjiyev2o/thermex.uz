from django.contrib import admin
from .models import City, Region, Notification
from modeltranslation.admin import TranslationAdmin


@admin.register(City)
class CityAdmin(TranslationAdmin):
    list_display = ('id', 'region', 'name')


@admin.register(Region)
class RegionAdmin(TranslationAdmin):
    list_display = ('id', 'name')


@admin.register(Notification)
class NotificationAdmin(TranslationAdmin):
    list_display = ('id', 'title', 'created_at')

