from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(blank=False, max_length=55)
    desc = models.TextField(blank=True, max_length=255)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name


