from django.shortcuts import render
from content.forms import TaskForm
from django.http import HttpResponseRedirect


def page(request):
    return render(request, "content/page.html")

def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("")
    else:
        form = TaskForm()
    return render(request, "content/create_task.html", {"form": form})