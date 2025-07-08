from django.shortcuts import render, get_object_or_404
from manager.models import Course


# Create your views here.
def checkout(request, title):
    course = get_object_or_404(Course, title=title)
    return render(request, 'checkout/checkout.html', {
        'course':course
    })