from django.core.validators import MaxValueValidator
from django.db import models
# Create your models here.

class Fields(models.Model):
    userName = models.CharField(max_length=100)
    videoNumbers = models.IntegerField()
    titleVideo = models.TextField()
    url = models.TextField()
    extension = models.CharField(max_length=100)
    sizeMB = models.IntegerField(
        default=1,
        validators=[
        MaxValueValidator(3),
    ])
    
    def __str__(self):
        return self.titleVideo
    