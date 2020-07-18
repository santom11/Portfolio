from django.shortcuts import render
from .models import Project


def all_projects(request):
    projects = Project.objects.all()
    return render(request, 'resume/all_projects.html', {'projects': projects})


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'resume/detail.html', {'project': project})