from django import forms
from .models import Customer, Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('adopter', 'name', 'age', 'kind', 'gender')
        widgets = {
            'adopter': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'kind': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name_surname', 'phone', 'mail')
        widgets = {
            'name_surname': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'mail': forms.EmailInput(attrs={'class': 'form-control'}),
        }