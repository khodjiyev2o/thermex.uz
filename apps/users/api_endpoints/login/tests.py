from rest_framework.test import APIRequestFactory, APITestCase

from apps.users.api_endpoints import PhoneVerificationView, PhoneAuthenticationView
from apps.users.models import VerificationCode


class SendAuthVerificationCodeViewTestCase(APITestCase):
    def test_send_verify_wrong_verification_code(self):
        """ Sending the code to number """
        view = PhoneAuthenticationView.as_view()
        data = {"phone": "+998945611911"}
        req = APIRequestFactory().post("/", data=data, format="json")
        response = view(req)
        self.assertEqual(response.data['success'], True)
        self.assertEqual(response.data['message'], f"Activation code successfully sent to {data['phone']}!")
        self.assertEqual(response.status_code, 201)
        """ Verifying the code """
        view = PhoneVerificationView.as_view()
        data = {"phone": "+998945611911", "code": "1111"}
        req = APIRequestFactory().post("/", data=data, format="json")
        response = view(req)
        self.assertEqual(response.data['code'][0], 'Неверный код')
        self.assertEqual(response.status_code, 400)

    def test_send_verify_correct_verification_code(self):
        """ Sending the code to number """
        view = PhoneAuthenticationView.as_view()
        data = {"phone": "+998945611911"}
        req = APIRequestFactory().post("/", data=data, format="json")
        response = view(req)
        self.assertEqual(response.data['success'], True)
        self.assertEqual(response.data['message'], f"Activation code successfully sent to {data['phone']}!")
        self.assertEqual(response.status_code, 201)
        """ Verifying the code """
        obj = VerificationCode.objects.get(phone=data['phone'])
        view = PhoneVerificationView.as_view()
        data = {"phone": "+998945611911", "code": f"{obj.code}"}
        req = APIRequestFactory().post("/", data=data, format="json")
        response = view(req)
        self.assertEqual(response.data['success'], True)
        self.assertEqual(response.data['message'], "Phone number verified successfully")
        self.assertEqual(list(response.data['tokens'].keys()), ['access', 'refresh'])
        self.assertEqual(response.status_code, 201)
