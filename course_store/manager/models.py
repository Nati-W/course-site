from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200)
    # validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mkv', 'mov', 'avi'])]
    video = models.FileField(upload_to='video/')
    thumbnail = models.ImageField(upload_to='thumbnail/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title