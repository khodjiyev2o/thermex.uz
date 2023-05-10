from django.contrib import admin
from .models import User, VerificationCode


@admin.register(VerificationCode)
class VerificationCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'code', 'expires_at',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'first_name', 'city', 'is_staff',)
    list_display_links = ('id', 'phone')
    list_filter = ('has_team', 'is_staff', 'created_at', 'city')
    search_fields = (
        'id',
        'email'
        'first_name',
        'last_name',
        'phone',
        'username',
    )




