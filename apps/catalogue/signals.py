import environ
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.products.models import UserBoughtProduct

from .utils import Eskiz


env = environ.Env()
email = env.str("ESKIZ_USER_EMAIL")
password = env.str("ESKIZ_USER_PASSWORD")


@receiver(post_save, sender=UserBoughtProduct)
def admin_send_sms_user_prize_signal(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        product = instance.thermex_product if instance.thermex_product else instance.prize_product
        user.points -= product.sell_point
        user.save()
        """Sending SMS via Eskiz"""
        custom_eskiz = Eskiz(instance=instance, password=password, email=email)
        custom_eskiz.send_sms_message_to_admin_and_user_about_user_prize()
