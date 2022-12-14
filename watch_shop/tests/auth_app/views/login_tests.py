from django.test import TestCase

from watch_shop.auth_app.models import AppUser


class LoginViewTests(TestCase):
    def test_view_logging_user(self):
        email = 'user@123.com'
        password = '1234;ds*S1'
        AppUser.object.create_user(email=email, password=password)
        self.client.login(username=email, password=password)  # defined in fixture or with factory in setUp()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
