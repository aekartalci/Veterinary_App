from .models import Pet, Customer
from .forms import PetForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView


class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class HomeView(ListView):
    template_name = 'index.html'
    model = Pet

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(name__icontains=query)
            if not object_list:
                object_list = self.model.objects.filter(adopter__name_surname__icontains=query)
            if not object_list:
                object_list = self.model.objects.filter(kind__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list


class PetCreate(CreateView):
    model = Pet
    form_class = PetForm
    template_name = 'create_pet.html'
    success_url = reverse_lazy('index')


class PetDetails(DetailView):
    model = Pet
    template_name = 'details.html'


class PetDelete(DeleteView):
    model = Pet
    template_name = 'delete_pet.html'
    success_url = reverse_lazy('index')


class PetUpdate(UpdateView):
    model = Pet
    template_name = 'update_pet.html'
    fields = ['adopter', 'name', 'age', 'kind', 'gender']


class Customers(ListView):
    model = Customer
    template_name = 'customers.html'


class CustomerUpdate(UpdateView):
    model = Customer
    template_name = 'update_customer.html'
    fields = ['name', 'surname', 'phone', 'mail']