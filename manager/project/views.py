from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Project


@login_required
def projects(request):
    projects = Project.objects.filter(created_by = request.user)
    return render(request, 'project/projects.html',
                  {
                      'projects':projects
                  })


@login_required
def get(request, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=pk)
    return render(request, 'project/project.html', {
        'project' : project
    })

@login_required
def add(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')

        if name:
            Project.objects.create(name=name, description=description, created_by=request.user)
            print(Project)
            return redirect('/projects')
        else:
            print("invalid data")

    return render(request, 'project/add.html')


@login_required
def edit(request, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name', '')
        description = request.POST.get('description', '')
        last_modified = timezone.now()

        if name:
            project.name = name
            project.description = description
            project.last_modified = last_modified
            project.save()

            return redirect('/projects')
    else:
        return render(request, 'project/edit.html',{
                      "project": project
                      })

@login_required
def delete(request, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=pk)
    project.delete()
    return redirect('/projects')