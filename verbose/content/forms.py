from django import forms
from content.models import Task

class TaskForm(forms.ModelForm):
    
    class Meta:
    constraints = [
        models.UniqueConstraint(
            fields=["date", "slot"],
            name="unique_user_day_slot"
        )
    ]
