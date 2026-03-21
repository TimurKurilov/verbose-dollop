from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(blank=False, max_length=55)
    slot = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name


