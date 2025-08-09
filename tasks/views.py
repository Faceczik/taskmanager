from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import RegisterForm
from .models import Task
from .forms import TaskForm


@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html',
                   {'form': form, 'task': task})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = RegisterForm()
    return render(request, 'tasks/register.html', {'form': form})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect('task_list')


def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.is_completed = not task.is_completed
    task.save()
    return redirect('task_list')


@login_required
def task_list(request):
    filter_type = request.GET.get("filter", "all")
    tasks = Task.objects.filter(user=request.user)

    if filter_type == "completed":
        tasks = tasks.filter(is_completed=True)
    elif filter_type == "active":
        tasks = tasks.filter(is_completed=False)

    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            print(f"✔️ is_completed: {task.is_completed}")
            task.save()
            return redirect('task_list')

    return render(request, 'tasks/task_list.html',
                   {'form': form, 'tasks': tasks})
