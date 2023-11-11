from django.urls import path
from .views import Home, PickupOrDelivery, Signup
from django.contrib.auth import views

urlpatterns = [
    path('', Home.as_view(),name='home'),
    path('pickup_delivery/', PickupOrDelivery.as_view(), name='pickup_delivery'),
    path('signup', Signup.as_view(), name='signup'),
    path('signin/', views.LoginView.as_view(template_name='bases/signin.html'),name='signin'),
    path('signout', views.LogoutView.as_view(template_name='bases/signin.html'), name='signout')
]