from django.utils import timezone
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib import messages
from content.forms import TaskForm
from content.models import Task


def page(request):
    return render(request, "content/page.html")

def create_task(request):
    if not request.user.is_authenticated:
        return redirect("login")
    tasks_count_by_date = Task.objects.filter(
        user=request.user,
        date__date = timezone.now().date(),
        ).count()
    if tasks_count_by_date >= 3:
        messages.error(request, f"На сегодня все братик")
        return redirect("all_task")

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.date = timezone.now()
            task.save()
            return HttpResponseRedirect("all_task")
    else:
        form = TaskForm()
    return render(request, "content/create_task.html", {"form": form})

def all_task(request):
    if not request.user.is_authenticated:
        return redirect("register")
    tasks = Task.objects.filter(user=request.user)
    return render(request, "content/all_tasks.html", {"tasks": tasks})