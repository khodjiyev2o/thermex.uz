from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.common.models import Notification
from fcm_django.models import FCMDevice


@receiver(post_save, sender=Notification)
def cliente_create_signal(sender, instance, created, **kwargs):
    if created:
        from firebase_admin.messaging import Message, Notification
        message = Message(
            notification=Notification(title=instance.title_uz, body=instance.text_uz,
                                      image=instance.image.url if instance.image else None),
        )
        FCMDevice.objects.send_message(message)

