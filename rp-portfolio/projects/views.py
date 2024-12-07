from django.shortcuts import render
from projects.models import Project

# Create your views here.

# This function retrieves all projects from the database using `Project.objects.all()`.
# It then stores the list of projects in the `context` dictionary with the key "projects".
# The context is passed to the "projects/project_index.html" template to display the list of all projects.
def project_index(request):
    projects = Project.objects.all()
    context = {
        "projects": projects
    }
    return render(request, "projects/project_index.html", context)


# This function retrieves a specific project from the database using the `pk` (primary key) parameter.
# It then stores the project instance in the `context` dictionary with the key "project".
# The context is passed to the "projects/project_detail.html" template for rendering the project's details.
def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        "project": project
    }
    return render(request, "projects/project_detail.html", context)