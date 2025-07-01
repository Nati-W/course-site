from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from . import forms


# Create your views here.
def shop(request):
    return render(request, 'shop/shop.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            login(request, form.save())
            return
    else:
        form = UserCreationForm()
    return render(request, 'shop/register.html', {
        'form':form
    })

def login_(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return
    else:
        form = AuthenticationForm()
    return render(request, 'shop/login.html', {
        'form':form
    })

def logout_(request):
    if request.method == 'POST':
        logout(request)
    return