from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .forms import AddressForm
from django.views import generic
from django.urls import reverse_lazy
from .models import Address

# Create your views here.
class AddressView(generic.CreateView):
    template_name = 'cmp/address_form.html'
    context_object_name = 'obj'
    form_class = AddressForm
    success_url = reverse_lazy('cmp:address_list')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class AddressList(generic.ListView):
    template_name = 'cmp/address_list.html'
    model = Address
    context_object_name = 'obj'
    def get_queryset(self):
        user = self.request.user
        address = super().get_queryset()
        address = address.filter(user=user)
        return address