from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('<str:title>', views.checkout, name='checkout')
]
