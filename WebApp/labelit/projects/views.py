from django.shortcuts import render
from .models import Project
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {}

    if request.user.is_authenticated:
        projects = Project.objects.filter(user=request.user)
        context = {'projects': projects}

    return render(request, 'projects/index.html', context)
    #return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, project_id):
    project = Project.objects.filter(id=project_id)[0]
    context = {'project': project}
    return render(request, 'projects/detail.html', context)