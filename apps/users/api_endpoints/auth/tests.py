from rest_framework.test import APIRequestFactory, APITestCase

from apps.users.api_endpoints.auth import PhoneAuthenticationView


class SendAuthVerificationCodeViewTestCase(APITestCase):
    def test_send_auth_verification_code(self):
        view = PhoneAuthenticationView.as_view()
        data = {"phone": "+998945611911"}
        req = APIRequestFactory().post("/", data=data, format="json")
        response = view(req)
        self.assertEqual(response.data['success'], True)
        self.assertEqual(response.data['message'], f"Activation code successfully sent to {data['phone']}!")
        self.assertEqual(response.status_code, 201)
        """Sending authentication again during 5 minutes"""
        req2 = APIRequestFactory().post("/", data=data, format="json")
        response2 = view(req2)
        self.assertEqual(response2.data['success'], False)
        self.assertEqual(response2.data['message'], "Activation code already sent !")
        self.assertEqual(response2.status_code, 200)
