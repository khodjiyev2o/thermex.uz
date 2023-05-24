import random
import string
from eskiz_sms import EskizSMS
import sys


def send_activation_code_via_sms(phone: str, code: str):
    if "test" not in sys.argv:
        message_data = f"Thermex.uz uchun <#> Tasdiqlash kodi: {code}"
        email = "samandarkhodjiyev@gmail.com"
        password = "b9LHEGCG9fppE4B2D7rEexqk4AgYVMIUr10JKXP3"
        eskiz = EskizSMS(email=email, password=password)
        eskiz.send_sms(mobile_phone=phone[1:], message=message_data, from_whom='4546', callback_url=None)


def generate_code():
    return "".join(random.choice(string.digits) for _ in range(4))