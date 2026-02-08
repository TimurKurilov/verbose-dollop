from django.shortcuts import render
from content.forms import TaskForm
from content.models import Task
from django.http import HttpResponseRedirect


def page(request):
    return render(request, "content/page.html")

def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/list/")
    else:
        form = TaskForm()
    return render(request, "content/create_task.html", {"form": form})

def all_task(request):
    tasks = Task.objects.all()
    return render(request, "content/all_tasks.html", {"tasks": tasks})