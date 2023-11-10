from django.urls import path
from .views import Home, PickupOrDelivery

urlpatterns = [
    path('', Home.as_view(),name='home'),
    path('pickup_delivery/', PickupOrDelivery.as_view(), name='pickup_delivery')
]