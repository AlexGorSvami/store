from datetime import timedelta
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now

from users.models import EmailVerification, User


class UserRegistrationViewTestCase(TestCase):
    def setUp(self):
        self.path = reverse('users:registration')
        self.data = {
            'first_name': 'Valera', 'last_name': 'Rebrov',
            'username': 'Volik', 'email': 'volik@yandex.ru',
            'password1': '1234567pO', 'password2': '1234567pO'
        }

    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - регистрация')
        self.assertTemplateUsed(response, 'users/registration.html')

    def test_user_registartion_post_success(self):
        response = self.client.post(self.path, self.data)

        username = self.data['username']
        # check creating of user
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(User.objects.filter(username=username).exists())

        # chek creating of email verification
        email_verification = EmailVerification.objects.filter(user__username=username)
        self.assertTrue(email_verification.exists())
        self.assertEqual(
            email_verification.first().expiration.date(),
            (now() + timedelta(hours=48)).date()
        )

    def test_user_registration_post_error(self):
        response = self.client.post(self.path, self.data)

        self.assertContains(response, 'Пользователь с таким именем уже существует.', html=True)
