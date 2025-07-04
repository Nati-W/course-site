from django.shortcuts import render, redirect
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