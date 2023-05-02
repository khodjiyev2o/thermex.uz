from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'region', 'is_staff',)
    list_display_links = ('id', )
    list_filter = ('has_team', 'is_staff', 'created_at')
    search_fields = (
        'id',
        'email',
        'first_name',
        'last_name',
        'phone',
        'username',
    )




