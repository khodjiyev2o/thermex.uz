from django.db.models.signals import post_save
from django.dispatch import receiver
from fcm_django.models import FCMDevice
from firebase_admin.messaging import Message, Notification

from apps.common.models import Notification as Noti


@receiver(post_save, sender=Noti)
def cliente_create_signal(sender, instance, created, **kwargs):
    if created:
        message = Message(
            notification=Notification(title=instance.title_uz, body=instance.text_uz),
        )
        devices = FCMDevice.objects.all()
        devices.send_message(message)
