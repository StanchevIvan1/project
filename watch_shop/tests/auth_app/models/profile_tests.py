from django.test import TestCase

from watch_shop.auth_app.models import AppUser, Profile


class ProfileCreateTests(TestCase):

    def test_profile_created_when_user_created(self):
        user = AppUser(
            email='test@mail.com',
            password='123@A12*12',
        )
        user.full_clean()
        user.save()

        profile = Profile(
            first_name='test',
            last_name='test',
            age=19,
            user=AppUser.object.get(id=user.id)
        )
        profile.full_clean()
        profile.save()
        print(Profile.objects.filter(user_id=profile.user_id).get())
        self.assertIsNotNone(Profile.objects.get(user_id=profile.user_id))

    def test_profile_info_can_be_changed(self):
        user = AppUser(
            email='test@mail.com',
            password='123@A12*12',
        )
        user.full_clean()
        user.save()

        first_name = 'test'
        last_name = 'test1'
        age = 20
        user = AppUser.object.get(id=user.id)

        profile = Profile(
            first_name=first_name,
            last_name=last_name,
            age=age,
            user=user
        )
        profile.full_clean()
        profile.save()

        self.assertEqual(first_name, profile.first_name)
        self.assertEqual(last_name, profile.last_name)
        self.assertEqual(age, profile.age)
        self.assertEqual(user.pk, profile.user_id)

    def test_profile__can_be_deleted__expected_user_to_be_deleted(self):
        user = AppUser(
            email='test@mail.com',
            password='123@A12*12',
        )
        user.full_clean()
        user.save()

        first_name = 'test'
        last_name = 'test1'
        age = 20
        user = AppUser.object.get(id=user.id)

        profile = Profile(
            first_name=first_name,
            last_name=last_name,
            age=age,
            user=user
        )
        profile.full_clean()
        profile.save()
        with self.assertRaises(Exception) as ex:
            profile.delete()
            user.objects.get(pk=profile.user_id)

        self.assertIsNotNone(ex.exception)
