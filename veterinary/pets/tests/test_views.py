from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

from pets.models import Pet, Customer


def create_user(client):
    User.objects.get_or_create(name='instructor')
    data = {
        'email': 'aekartalci@gmail.com',
        'password': 'KD0Kef72zvq*',
        'password2': 'KD0Kef72zvq*'
    }

    client.post(reverse('users:register'), data=data)


def login_user(client):
    logged_in: client.post(reverse('users:login'),
                           data={
                               'username': 'aekartalci@gmail.com',
                               'password': 'KD0Kef72zvq*',
                           })

class TestViews(TestCase):
    def setup(self):
        self.client = Client()
        self.adopter = Customer.objects.create(name_surname='Ahmet Kartalci',
                                               phone='+905916576266',
                                               mail='aekartalci@gmail.com')
        create_user(self.client)
        logged_in = login_user(self.client)
        self.user = logged_in

    def test_home_page(self):
        response = self.client.get('http://127.0.0.1:8000')
        self.assertEqual(response.status_code, 200)

    def test_register_page(self):
        response = self.client.get('http://127.0.0.1:8000/register/')
        self.assertEqual(response.status_code, 200)

"""    def test_pet_creation(self):
        self.adopter = Customer.objects.create(name_surname='Ahmet Kartalci',
                                               phone='+905462341212',
                                               mail='aekartalcix@gmail.com')
        data = {
            'adopter':self.adopter,
            'name':'lorem',
            'age':3,
            'description':'Lorem ipsum..',
            'kind':'cat',
            'gender':'male'
        }

        url = reverse('pets:create-pet')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200),
        self.assertTemplateUsed(response=response, template_name='create_pet.html')"""



