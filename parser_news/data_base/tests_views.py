from django.test import TestCase
from django.test import Client
from faker import Faker
from usersapp.models import Parser_User

class OpenViewsTest(TestCase):

    def setup(self):
        self.client = Client()
        self.fake = Faker()

    def test_statuses(self):
        responce = self.client.get('/')
        self.assertEqual(responce.status_code, 200)

        responce = self.client.get('/result_bv/')
        self.assertEqual(responce.status_code, 302)

        responce = self.client.get('/users/login/')
        self.assertEqual(responce.status_code, 200)

        responce = self.client.get('/users/register/')
        self.assertEqual(responce.status_code, 200)

    def test_login_required(self):
        Parser_User.objects.create_user(username='test_user', email='test@test.com', password='baha12345')
        responce = self.client.get('/result_bv/')
        self.assertEqual(responce.status_code, 302)





