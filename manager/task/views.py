from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from todolist.models import TodoList
from project.models import Project

@login_required
def task(request, project_id, todolist_id, pk):
    project = Project.objects.filter(created_by=request.user).get(id=project_id)
    todolist = TodoList.objects.filter(project=project).get(id=todolist_id)
    task = Task.objects.filter(project=project).filter(todolist=todolist).get(id=pk)
    return render(request, 'task/task.html', {
        'task' : task
    })

@login_required
def add(request, project_id, todolist_id):
    project = Project.objects.filter(created_by=request.user).get(id=project_id)
    todolist = TodoList.objects.filter(project=project).get(id=todolist_id)
    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')
        is_done = request.POST.get('is_done', False) == 'on'
        if name:
            Task.objects.create(name=name, description=description, is_done=is_done, created_by=request.user, project = project, todolist=todolist)
            return redirect(f'/projects/{project_id}/{todolist_id}/')
        print("invalid data posted")
    return render(request, 'task/add.html')

@login_required
def edit(request, project_id, todolist_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todolist = TodoList.objects.filter(project=project).get(pk=todolist_id)
    task = Task.objects.filter(project=project).filter(todolist=todolist).get(pk=pk)
    print(request.method)
    if request.method == "POST":
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')
        is_done = request.POST.get('is_done') == 'on'
        if name:
            task.name = name
        task.description = description
        task.is_done = is_done
        task.save()

        return redirect(f'/projects/{project_id}/{todolist_id}/{pk}/')
    print("invalid data posted")
    return render(request, 'task/edit.html', {
                'task': task
    })

@login_required
def delete(request, project_id, todolist_id, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    todolist = TodoList.objects.filter(project=project).get(pk=todolist_id)
    task = Task.objects.filter(project=project).filter(todolist=todolist).get(pk=pk)
    task.delete()
    return redirect(f'/projects/{project_id}/{todolist_id}/')