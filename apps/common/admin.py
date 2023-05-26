from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import City, Notification, Region


@admin.register(City)
class CityAdmin(TranslationAdmin):
    list_display = ("id", "region", "name")


@admin.register(Region)
class RegionAdmin(TranslationAdmin):
    list_display = ("id", "name")


@admin.register(Notification)
class NotificationAdmin(TranslationAdmin):
    list_display = ("id", "title", "created_at")
