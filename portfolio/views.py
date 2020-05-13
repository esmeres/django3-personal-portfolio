from django.shortcuts import render
# the class Project (table in the database) in the models.py file will be imported here
from .models import Project



# Create your views here.

def home(request):
# import the objects in the homepage of which we created in the models.py
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})

