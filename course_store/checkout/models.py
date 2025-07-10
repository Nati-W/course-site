from django.db import models
from django.contrib.auth.models import User
from manager.models import Course

# Create your models here.
class CustomerInfo(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    card_info = models.CharField()
    