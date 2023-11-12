from django.urls import path
from .views import AddressView, AddressList

urlpatterns = [
    path('address_list', AddressList.as_view(), name = 'address_list'),
    path('address_form/', AddressView.as_view(), name='address_form'),
]