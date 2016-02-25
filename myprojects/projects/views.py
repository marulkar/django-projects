from django.shortcuts import render, render_to_response

from projects.models import Projects

# Create your views here.

def Project(request, projects_id):
	return render_to_response('Project.html', {'Project' :Projects.objects.get(id = projects_id)})

def All(request):
	return render_to_response('Projects.html', {'Projects' : Projects.objects.all()})