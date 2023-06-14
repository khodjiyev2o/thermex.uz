import sys

import environ
from celery import shared_task
from eskiz_sms import EskizSMS


env = environ.Env()


@shared_task()
def send_activation_code_via_sms(phone: str, code: str):
    # Celery recognizes this as the `apps.users.tasks.send_activation_code_via_sms` task
    if "test" not in sys.argv:
        message_data = f"Thermex.uz uchun <#> Tasdiqlash kodi: {code}"
        email = env.str("ESKIZ_USER_EMAIL")
        password = env.str("ESKIZ_USER_PASSWORD")
        eskiz = EskizSMS(email=email, password=password)
        eskiz.send_sms(mobile_phone=phone[1:], message=message_data, from_whom="4546", callback_url=None)
