from django.utils import timezone
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib import messages
from content.forms import TaskForm
from content.models import Task


slots = {1,2,3}

def page(request):
    return render(request, "content/page.html")

def create_task(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    if Task.objects.filter(
        user=request.user,
        date__date = timezone.now().date(),
        slot = 0
        ):
            messages.error(request, f"На сегодня все братик")
            return redirect("all_task")
    
    taken = set(
    Task.objects.filter(
        user=request.user,
        date__date=timezone.now().date()
    ).values_list("slot", flat=True)
    )
    
    free_slot = min(slots - taken)

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.date = timezone.now()
            task.slot = free_slot
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

def task_by_date(request, datee):
    tasks_by_date = Task.objects.filter(user=request.user, date__date=datee)
    return render(request, "content/tasks_by_date", {"tasks_by_date", tasks_by_date})    