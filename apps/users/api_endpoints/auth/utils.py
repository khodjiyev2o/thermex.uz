import random
import string


def send_activation_code_via_sms(phone: str, code: str):
    pass


def generate_code():
    return "".join(random.choice(string.digits) for _ in range(4))