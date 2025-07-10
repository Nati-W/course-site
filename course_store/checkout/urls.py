from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('<str:title>', views.checkout, name='checkout'),
    path('<str:title>/register', views.unregistered_checkout, name='unregistered_checkout')
]
