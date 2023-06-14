import sys

import environ
from celery import shared_task
from eskiz_sms import EskizSMS

from apps.products.models import UserBoughtProduct
from apps.users.models import User


env = environ.Env()
email = env.str("ESKIZ_USER_EMAIL")
password = env.str("ESKIZ_USER_PASSWORD")


@shared_task()
def update_point_count(instance_id: int) -> None:
    instance = UserBoughtProduct.objects.get(id=instance_id)
    product = instance.thermex_product if instance.thermex_product else instance.prize_product
    user = instance.user

    user.points -= product.sell_point
    user.save()


@shared_task()
def send_message_to_user_and_admins(instance_id: int) -> None:
    instance = UserBoughtProduct.objects.get(id=instance_id)
    product = instance.thermex_product if instance.thermex_product else instance.prize_product
    user = instance.user

    user_message = (
        f"Tabriklaymiz, siz muvaffaqiyatli {product.name} sotib oldingiz, "
        f"{product.sell_point} "
        f"ballga sotib oldingiz. Thermex.uz jamoasi yaqin vaqt ichida sizga aloqaga chiqadi"
    )
    admin_message = (
        f"{user.phone} dagi foydalanuvchi, {product.name} " f"mahsulotni {product.sell_point} ballga sotib oldi"
    )

    eskiz = EskizSMS(email=email, password=password)

    if "test" not in sys.argv:
        # Sending sms to user
        eskiz.send_sms(
            mobile_phone=str(instance.user.phone)[1:],
            message=user_message,
            from_whom="4546",
            callback_url=None,
        )
        # Sending sms to admins about user purchase
        for user in User.objects.filter(is_superuser=True):
            eskiz.send_sms(mobile_phone=str(user.phone)[1:], message=admin_message, from_whom="4546", callback_url=None)
