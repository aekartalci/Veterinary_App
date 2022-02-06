from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
from ckeditor.fields import RichTextField


class Customer(models.Model):
    name_surname = models.CharField(max_length=100)
    phone = PhoneNumberField(unique=True, null=False, blank=False)
    mail = models.EmailField(max_length=255)

    def __str__(self):
        return self.name_surname

    def get_absolute_url(self):
        return reverse('index')


class Pet(models.Model):
    class AnimalKind(models.TextChoices):
        CAT = 'cat', 'Kedi'
        DOG = 'dog', 'Köpek'
        EXOTIC = 'exotic', 'Egzotik'
        WINGED = 'winged', 'Kanatlı'
        TROPICAL = 'tropical', 'Tropikal'
        WILD = 'wild', 'Yabani'
        OTHER = 'other', 'Diğer'

    class AnimalGender(models.TextChoices):
        MALE = 'male', 'Erkek'
        FEMALE = 'female', 'Dişi'

    adopter = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    description = RichTextField(blank=True, null=True)

    kind = models.CharField(
        max_length=20,
        choices=AnimalKind.choices,
        default=AnimalKind.OTHER
    )
    gender = models.CharField(
        max_length=20,
        choices=AnimalGender.choices,
        default=AnimalGender.FEMALE
    )


    def __str__(self):
        return self.name + "|" + self.kind

    def get_absolute_url(self):
        return reverse('index')