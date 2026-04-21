from datetime import datetime

from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect, render
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
    
    today = timezone.now().date()
    
    taken_slots = Task.objects.filter(
        user=request.user,
        day=today
    ).values_list("slot", flat=True)
    
    taken = set(
        Task.objects.filter(
            user=request.user,
            day=today
        ).values_list("slot", flat=True)
    )
    
    taken = set(taken_slots)
    if len(taken) >= len(slots):
        messages.error(request, "На сегодня лимит задач достигнут")
        return redirect("list")

    free_slot = min(slots - taken)

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.day = today
            task.slot = free_slot
            task.save()
            return redirect("list")
    else:
        form = TaskForm()

    return render(request, "content/create_task.html", {"form": form})

def all_task(request):
    if not request.user.is_authenticated:
        return redirect("login")
    tasks = Task.objects.filter(user=request.user)
    return render(request, "content/all_tasks.html", {"tasks": tasks})

def tasks_by_date(request, date):
    parsed_date = datetime.strptime(date, "%Y-%m-%d").date()
    tasks_by_date = Task.objects.filter(user=request.user, day=parsed_date)
    return render(request, "content/tasks_by_date.html", {"tasks_by_date": tasks_by_date})

def tasks_by_date_and_slot(request, date, slot):
    parsed_date = datetime.strptime(date, "%Y-%m-%d").date()
    tasks_by_date_and_slot = Task.objects.filter(user=request.user, day=parsed_date, slot=slot)
    return render(request, "content/tasks_by_date_and_slot.html", {"tasks_by_date_and_slot": tasks_by_date_and_slot})

def task_delete(request, date, slot):
    parsed_date = datetime.strptime(date, "%Y-%m-%d").date()
    if not request.user.is_authenticated:
        return redirect("login")
    task = get_object_or_404(Task, day=parsed_date, slot=slot, user=request.user)
    task.delete()
    return redirect("list")

def task_edit(request, date, slot):
    parsed_date = datetime.strptime(date, "%Y-%m-%d").date()
    task = get_object_or_404(Task, day=parsed_date, slot=slot)
    if task.user != request.user:
        return redirect("list/")
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save
            return redirect("list/")
    else:
        form = TaskForm(instance=task)
    return render(request, "content/task_edit.html", {"tasks_edit": form})