from django.shortcuts import render
from django.views import generic

# Create your views here.
class Home(generic.TemplateView):
    template_name='bases/home.html'

class PickupOrDelivery(generic.TemplateView):
    template_name = 'bases/pickup_or_delivery.html'