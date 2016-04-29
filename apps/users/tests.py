from django.test import TestCase, Client

# Create your tests here.
class TestUsers(TestCase):

    def setUp(self):
        self.client = Client()

    def test_user_can_be_created_with_username_password(self):
        data = {'username': 'User', 'password': 'password'}

        response = self.client.post('/users', data=data)

        self.assertEqual(response.status_code, 201)
