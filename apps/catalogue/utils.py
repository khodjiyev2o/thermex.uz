import sys

from apps.common.utils import MyEskiz

from apps.users.models import User


class Eskiz:
    def __init__(self, password, email, instance):
        self.email = email
        self.password = password
        self.instance = instance
        self.product = instance.thermex_product if instance.thermex_product else instance.prize_product
        self.admin_message = (
            f"{self.instance.user.phone} dagi foydalanuvchi, {self.product.name} "
            f"mahsulotni {self.product.sell_point} ballga sotib oldi"
        )
        self.user_message = (
            f"Tabriklaymiz, siz muvaffaqiyatli {self.product.name} sotib oldingiz, "
            f"{self.product.sell_point} "
            f"ballga sotib oldingiz. Thermex.uz jamoasi yaqin vaqt ichida sizga aloqaga chiqadi"
        )

    def send_sms_message_to_admin_and_user_about_user_prize(self):
        eskiz = MyEskiz(email=self.email, password=self.password)
        if "test" not in sys.argv:
            eskiz.send_sms(
                mobile_phone=str(self.instance.user.phone)[1:],
                message=self.user_message,
            )
            for user in User.objects.filter(is_superuser=True):
                eskiz.send_sms(mobile_phone=str(user.phone)[1:], message=self.admin_message)
