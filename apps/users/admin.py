from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'first_name', 'region', 'is_staff',)
    list_display_links = ('id', 'phone')
    list_filter = ('has_team', 'is_staff', 'created_at', 'region')
    search_fields = (
        'id',
        'email'
        'first_name',
        'last_name',
        'phone',
        'username',
    )




