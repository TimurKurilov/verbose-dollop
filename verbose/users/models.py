from django.db import models

# Create your models here.

class Creation(models.Model):
    username = models.CharField(max_length=20, unique=True)