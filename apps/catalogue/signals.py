from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.products.models import UserBoughtProduct

from .tasks import send_message_to_user_and_admins, update_point_count


@receiver(post_save, sender=UserBoughtProduct)
def admin_send_sms_user_prize_signal(sender, instance, created, **kwargs):
    if created:
        update_point_count.delay(instance_id=instance.id)
        send_message_to_user_and_admins.delay(instance_id=instance.id)
