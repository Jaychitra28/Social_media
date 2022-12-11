from django.test import TestCase, Client
from .test_model_mixin import ModelMixinTestCase
from django.urls import reverse
from django.contrib.auth.models import User
from account.forms import UserRegistrationForm
from django.contrib.auth import get_user_model


class UserLogin(ModelMixinTestCase, TestCase):
    def test_account_dashboard_GET(self):
        self.client = Client()
        self.assertTrue(self.user.is_active)
        self.client.login(username="jaya", password="1234")
        response = self.client.get(reverse("dashboard"))

        self.assertTemplateUsed(response, "account/dashboard.html")


class UserRegister(ModelMixinTestCase, TestCase):
    def test_user_regiter_returns_registrationform(self):
        response = self.client.get(reverse("register"))

        self.assertEqual(response.context.get("form"), UserRegistrationForm)

    def test_templates_used_with_register_account(self):

        response = self.client.get(reverse("register"))
        self.assertTemplateUsed(
            response, "account/register.html", "account/register_done.html"
        )

    def test_register_succeeds_registering_users_with_valid_credentials(self):
        self.client.post(
            reverse("register"),
            data={
                "username": "Jayachitra",
                "first_name": "Jayachitra",
                "email": "jayachitra@example.com",
                "password": "123",
                "password2": "123",
            },
        )
        self.assertTrue(User.objects.filter(username="Jayachitra").exists())


class ProfileEdit(ModelMixinTestCase, TestCase):
    def test_template_used_with_edit_profile(self):
        self.client.login(username="sowmiya", password="password")
        response = self.client.get(reverse("edit"))

        self.assertTemplateUsed(response, "account/edit.html")

    def test_editing_user_profile_succeds(self):

        self.client.login(username="sowiya", password="password")
        self.client.post(
            reverse("edit"),
            data={
                "first_name": "Jayachitra",
            },
        )
        user = User.objects.get(username="sowmiya")
        self.assertEqual(user.first_name, "Jayachitra")
