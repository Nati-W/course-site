from django import forms
from . import models

class UploadCourse(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = ['title', 'video', 'thumbnail', 'price']