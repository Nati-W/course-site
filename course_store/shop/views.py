from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from manager.models import Course


# Create your views here.
def shop(request):
    courses = Course.objects.all()
    return render(request, 'shop/shop.html', {
        'courses':courses
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            auth_login(request, form.save())
            return redirect('shop:shop')
    else:
        form = UserCreationForm()
    return render(request, 'shop/register.html', {
        'form':form
    })

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('shop:shop')
    else:
        form = AuthenticationForm()
    return render(request, 'shop/login.html', {
        'form':form
    })

def logout(request):
    if request.method == 'POST':
        auth_logout(request)
    return redirect('shop:shop')