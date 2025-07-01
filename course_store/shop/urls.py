from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.shop),
    path('register', views.register, name='register'),
    path('login', views.login_, name='login'),
    path('', views.logout_, name='logout'),
]
