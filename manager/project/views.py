from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Project, ProjectFile

from .forms import ProjectFileForm


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

            return redirect(f'/projects/{pk}')
    else:
        return render(request, 'project/edit.html',{
                      "project": project
                      })

@login_required
def delete(request, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=pk)
    project.delete()
    return redirect('/projects')


@login_required
def upload_file(request, pk):
    project = Project.objects.filter(created_by=request.user).get(pk=pk)
    
    if request.method == 'POST':
        form = ProjectFileForm(request.POST, request.FILES)

        if form.is_valid():
            projectfile = form.save(commit=False)
            projectfile.project = project
            projectfile.save()
            print(projectfile.id, projectfile.name)
            return redirect(f'/projects/{pk}/')
    else:
        form = ProjectFileForm()
    
    return render(request, 'project/upload_file.html',{
        'project' : project,
        'form' : form
    }) 


@login_required
def delete_file(request, project_id=None, pk=None):
    project = Project.objects.filter(created_by=request.user).get(pk=project_id)
    projectfile = project.files.get(pk=pk)
    print("project :", project.id)
    print("file id: ", projectfile.id)
    print("file name: ",projectfile.name)
    projectfile.delete()
    
    return redirect(f'/projects/{project_id}/')
