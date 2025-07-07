from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    path('', views.manage, name='manage'),
    path('upload', views.upload, name='upload-course'),
    path('edit-list', views.edit_list, name='edit-list'),
    path('edit/<int:course_id>', views.edit_course, name='edit')
]
