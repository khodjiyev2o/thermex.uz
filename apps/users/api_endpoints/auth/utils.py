import random
import string
from eskiz_sms import EskizSMS
import sys
import environ
env = environ.Env()


def send_activation_code_via_sms(phone: str, code: str):
    if "test" not in sys.argv:
        message_data = f"Thermex.uz uchun <#> Tasdiqlash kodi: {code}"
        email = env.str('ESKIZ_USER_EMAIL')
        password = env.str('ESKIZ_USER_PASSWORD')
        eskiz = EskizSMS(email=email, password=password)
        eskiz.send_sms(mobile_phone=phone[1:], message=message_data, from_whom='4546', callback_url=None)


def generate_code():
    return "".join(random.choice(string.digits) for _ in range(4))