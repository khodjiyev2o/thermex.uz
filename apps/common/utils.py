import requests


class MyEskiz:
    login_url = "https://notify.eskiz.uz/api/auth/login"
    send_sms_url = "https://notify.eskiz.uz/api/message/sms/send"

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def _get_auth_token(self):
        payload = {"email": self.email, "password": self.password}
        files = []
        headers = {}

        response = requests.request("POST", self.login_url, headers=headers, data=payload, files=files)

        return response.json()["data"]["token"]

    @staticmethod
    def _get_authorization_header(token):
        return {"Authorization": f"Bearer {token}"}

    def send_sms(self, mobile_phone: str, message: str):
        payload = {"mobile_phone": mobile_phone, "message": message, "from": "4546", "callback_url": None}
        files: list = []
        headers = self._get_authorization_header(token=self._get_auth_token())

        response = requests.request("POST", self.send_sms_url, headers=headers, data=payload, files=files)

        print(response.json()["message"])
