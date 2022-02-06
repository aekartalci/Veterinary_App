from django.test import TestCase
from pets.models import Customer, Pet


class TestModels(TestCase):
    def setUp(self):
        self.adopter = Customer.objects.create(name_surname='Ahmet Kartalci',
                                               phone='+905916576266',
                                               mail='aekartalci@gmail.com')

        self.pet = Pet.objects.create(
            adopter=self.adopter,
            name='lorem',
            age=3,
            description='Lorem ipsum..',
            kind='cat',
            gender='male'
        )

    def test_pet_creation(self):
        pet=self.pet
        adopter=self.adopter
        self.assertTrue(isinstance(pet, Pet))
        self.assertIsInstance(self.pet.age, int)
        self.assertEqual(adopter.phone, '+905916576266')


