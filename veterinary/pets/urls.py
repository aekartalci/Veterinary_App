from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView, PetDetails, PetCreate, PetUpdate, PetDelete, Customers, CustomerUpdate, UserRegisterView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
        path('', HomeView.as_view(), name="index"),
        path('pet/<int:pk>', PetDetails.as_view(), name="pet-detail"),
        path('create_pet/', PetCreate.as_view(), name="create-pet"),
        path('pet/edit/<int:pk>', PetUpdate.as_view(), name="update-pet"),
        path('pet/<int:pk>/delete', PetDelete.as_view(), name="delete-pet"),
        path('customer/<int:pk>', Customers.as_view(), name="customer-detail"),
        path('customer/edit/<int:pk>', CustomerUpdate.as_view(), name="update-customer"),
        path('register/', UserRegisterView.as_view(), name="register"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)