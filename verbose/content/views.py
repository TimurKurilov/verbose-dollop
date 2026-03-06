from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib import messages
from content.forms import TaskForm
from content.models import Task


def page(request):
    return render(request, "content/page.html")

def create_task(request):
    tasks_count = Task.objects.all(owner=request.user).count()
    if tasks_count > 3:
        messages.error(request, f"На сегодня все братик")
        return redirect("all_task")

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/list/")
    else:
        form = TaskForm()
    return render(request, "content/create_task.html", {"form": form})

def all_task(request):
    tasks = Task.objects.all(owner=request.user)
    if not request.user.is_authenticated:
        return redirect("register")
    return render(request, "content/all_tasks.html", {"tasks": tasks})