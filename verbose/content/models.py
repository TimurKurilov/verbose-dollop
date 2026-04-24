from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    slot = models.IntegerField(default=1)
    day = models.DateField()
    is_completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "day", "slot"],
                name="unique_user_day_slot"
            )
        ]
        
    def __str__(self):
        return f"{self.user} : {self.name} | slot={self.slot} | day={self.day} | created={self.created}"