"""Tests for all models in our API"""

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

class UserTests(TestCase):
    """Tests for the user model"""

    def test_create_user(self):
        """Tests creating a user is successful"""

        email = 'test@example.com'
        password = 'testpass123'

        user = get_user_model().objects.create_user(
            email=email, password=password
        )

        self.assertTrue(user.check_password(password))
        self.assertEqual(user.email, email)


    def test_normalize_email(self):
        """Test email is normalized when a user is created"""

        password = 'testpass123'

        test_emails = [
            ('test1@EXAMPLE.COM', 'test1@example.com'),
            ('test2@EXAMPLE.COM', 'test2@example.com'),
            ('test3@EXAMPLE.COM', 'test3@example.com'),
            ('test4@EXAMPLE.COM', 'test4@example.com')
        ]

        for email, expected in test_emails:
            user = get_user_model().objects.create_user(
                email=email, password=password
            )

            self.assertEqual(user.email, expected)

    def test_create_superuser(self):
        """Test creating a superuser is successful"""

        email = 'test@example.com'
        password = 'testpass123'

        user = get_user_model().objects.create_superuser(
            email=email, password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_user_without_email_raises_error(self):
        """Test ValueError raised when user created without email"""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email = "",
                password = "testpass123"
            )