from django.shortcuts import render, redirect, get_object_or_404

from .models import Task


def index(request):
    if request.method == "POST":
        task_content = request.POST.get("content", "").strip()
        priority = request.POST.get("priority")
        due_date = request.POST.get("due_date")

        if task_content and priority and due_date:
            Task.objects.create(
                content=task_content,
                priority=priority,
                due_date=due_date,
            )
            return redirect("index")

    tasks = Task.objects.all().order_by("due_date", "created_at")
    return render(request, "index.html", {"tasks": tasks})


def edit(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        task.content = request.POST.get("content", "").strip()
        task.priority = request.POST.get("priority", task.priority)
        task.due_date = request.POST.get("due_date", task.due_date)
        task.save()
        return redirect("index")

    return render(request, "edit.html", {"task": task})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect("index")
