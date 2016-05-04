from django.db import models
from django.utils import timezone

# Create your models here.

class ToDo(models.Model):
    text = models.TextField()
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)
    # timezone.now - the time when the intstance was created
    #  timezone.now() - the current time
    
