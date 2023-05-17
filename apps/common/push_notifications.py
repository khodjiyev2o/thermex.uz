from django.contrib import admin
from fcm_django.models import FCMDevice


def send_push_notifications(modeladmin, request, queryset):
    # Retrieve the message you want to send
    message = "Your push notification message"

    # Send the push notification to all selected devices
    for device in queryset:
        device.send_message(title="Notification Title", body=message)
        print("sent successfully message to  device:", device)


send_push_notifications.short_description = "Send push notifications"

class DeviceAdmin(admin.ModelAdmin):
    actions = [send_push_notifications]


admin.site.register(FCMDevice, DeviceAdmin)
