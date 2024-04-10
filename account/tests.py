from django.test import TestCase, Client
from django.contrib.auth.models import User
from account.serializers import RegisterSerializer

from rest_framework import status
import json

class RegisterSerializerTest(TestCase):
    def test_valid_registration(self):
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'password': 'password123'
        }
        serializer = RegisterSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, 'johndoe')

    def test_invalid_registration_username_taken(self):

        User.objects.create(username='johndoe')
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'password': 'password123'
        }
        serializer = RegisterSerializer(data=data)
        self.assertFalse(serializer.is_valid())


class RegisterViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register_valid_data(self):
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'password': 'password123'
        }
        response = self.client.post('/api/account/register/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_invalid_data(self):
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe', 
            'password': 'password123'
        }
        response = self.client.post('/api/account/register/', data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

