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
    success_url = reverse_lazy('bases:home')
    def form_valid(self, form):
        return super().form_valid(form)
    
class AddressList(generic.ListView):
    template_name = 'cmp/address_list.html'
    model = Address
    context_object_name = 'obj'