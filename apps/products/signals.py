from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.products.models import SoldProduct


@receiver(post_save, sender=SoldProduct)
def admin_send_sms_user_prize_signal(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        product = instance.product

        if product.point:
            user.points += product.point
            user.save()
