# models.py
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    slot = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "date__date", "slot"],
                name="unique_user_day_slot"
            )
        ]
