from django.urls import path
from .views import AddressView

urlpatterns = [
    path('address_form/', AddressView.as_view(), name='address_form'),
]