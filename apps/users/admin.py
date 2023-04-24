from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_creator', 'is_staff',)
    list_display_links = ('id', )
    list_filter = ('is_creator', 'is_staff', 'created_at')
    search_fields = (
        'id',
        'email',
        'first_name',
        'last_name',
        'username',
    )






