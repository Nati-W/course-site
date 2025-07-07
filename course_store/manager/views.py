from django.shortcuts import render, redirect, get_object_or_404
from . import forms
from . import models

# Create your views here.
def manage(request):
    return render(request, 'manager/manage.html')

def upload(request):
    if request.method == 'POST':
        form = forms.UploadCourse(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop:shop')
    else:
        form = forms.UploadCourse()
    return render(request, 'manager/uploader.html', {
        'form':form
    })

def edit_list(request):
    courses = models.Course.objects.all()
    return render(request, 'manager/edit_list.html', {
        'courses':courses
    })

def edit_course(request, course_id):
    course = get_object_or_404(models.Course, id=course_id)
    if request.method == 'POST':
        form = forms.UploadCourse(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('manager:edit-list')
    else:
        form = forms.UploadCourse(instance=course)

    return render(request, 'manager/edit.html', {
        'form':form
    })