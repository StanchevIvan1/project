from django.core.exceptions import ValidationError
from django.test import TestCase

from watch_shop.auth_app.models import AppUser


class AppUserTests(TestCase):
    def test_user_save__when_email_is_valid_expect_correct_result(self):
        user = AppUser(
            email='test@mail.com',
            password='123@A12*12',
        )

        user.full_clean()
        user.save()

        self.assertIsNotNone(user.pk)

    def test_user_save__when_email_is_invalid_expect_exception(self):
        user = AppUser(
            email='testmail.com',
            password='123@A12*12',
        )

        with self.assertRaises(ValidationError) as ex:
            user.full_clean()
            user.save()

        self.assertIsNotNone(ex.exception)