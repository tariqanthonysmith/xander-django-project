

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:create')

def create_user(**params):
    """Create and return a test user"""

    return get_user_model().objects.create(**params)

class PublicUSerAPITests(TestCase):
    """Tets for unauthenticated requests"""

    def setUp(self):
        self.client = APIClient()

    def test_user_create_successful(self):

        payload = {
            'name': 'Test User',
            'email' : 'test@example.com',
            'password' : 'testpass123'
        }

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        user = get_user_model().objects.get(email=payload['email'])

        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

