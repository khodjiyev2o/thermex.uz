from django.contrib import admin
from .models import Region


@admin.register(Region)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'name')

