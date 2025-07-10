from django.shortcuts import render, get_object_or_404, redirect
from manager.models import Course
from shop.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import *
from .models import *


# Create your views here.
def checkout(request, title):
    course = get_object_or_404(Course, title=title)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)

        if form.is_valid():
            customer = form.save(commit=False)
            customer.name = request.user
            customer.course = course
            if CustomerInfo.objects.filter(name=request.user, course=course).exists():
                messages.warning(request, "You have already purchased this course.")
                return redirect('shop:shop')
            customer.save()
            return redirect('shop:shop')
    else:
        form = CheckoutForm()

    return render(request, 'checkout/checkout.html', {
        'course':course,
        'form':form,
    })

def unregistered_checkout(request, title):
    course = get_object_or_404(Course, title=title)

    if request.method == 'POST':
        registerform = RegisterForm(request.POST)
        checkoutform = CheckoutForm(request.POST)

        if registerform.is_valid() and checkoutform.is_valid():
            user = registerform.save() 
            auth_login(request, user)

            customer = checkoutform.save(commit=False)
            customer.name = request.user
            customer.course = course
            customer.save()
            return redirect('shop:shop')
    else:
        registerform = RegisterForm()
        checkoutform = CheckoutForm()
        

    return render(request, 'checkout/unregistered_checkout.html', {
        'register':registerform,
        'checkout':checkoutform,
        'course':course
    })