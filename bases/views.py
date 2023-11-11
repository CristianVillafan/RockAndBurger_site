from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.db import IntegrityError

# Create your views here.
class Home(generic.TemplateView):
    template_name='bases/home.html'

class PickupOrDelivery(generic.TemplateView):
    template_name = 'bases/pickup_or_delivery.html'

class Signup(generic.CreateView):
    template_name = 'bases/signup.html'
    context_object_name = 'obj'
    form_class = UserCreationForm
    success_url = reverse_lazy('bases:home')
    def form_valid(self, form):
        return super().form_valid(form)