from django.shortcuts import render, render_to_response

from projects.models import Projects

from forms import ProjectViewForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

# Create your views here.

def Project(request, projects_id):
	return render_to_response('Project.html', {'Project' :Projects.objects.get(id = projects_id)})

def All(request):
	return render_to_response('Projects.html', {'Projects' : Projects.objects.all()})

def create(request):
    if request.POST:
        form = ProjectViewForm(request.POST, request.FILES)
        if form.is_valid():
            a = form.save()	

            return HttpResponseRedirect('/projects/all')
    else:
        form = ProjectViewForm()
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render_to_response('create_project.html', args)