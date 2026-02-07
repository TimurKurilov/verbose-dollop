from django import forms
from content.models import Task

class TaskForm(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = ("name", "desc", "date")
