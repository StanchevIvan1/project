from django.test import TestCase
from django.urls import reverse

from watch_shop.auth_app.models import AppUser


class TestCalls(TestCase):
    def test___view__anonymous_expect_to_redirect_to_login(self):
        response = self.client.get('/products/', follow=True)
        self.assertRedirects(response, '/auth/sign-in/?next=/products/')

    def test_view_logged_user(self):
        email = 'user@123.com'
        password = '1234;ds*S1'
        AppUser.object.create_user(email=email, password=password)
        self.client.login(username=email, password=password)  # defined in fixture or with factory in setUp()
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 302)

    def test_homepage(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
