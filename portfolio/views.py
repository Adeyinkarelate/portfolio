from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Project
from django.core.paginator import Paginator

# Create your views here.
def home_view(request):   
   all_projects = Project.objects.all().order_by('-time_created')
   p = Paginator(all_projects, 3)
   page = request.GET.get('page')
   projects = p.get_page(page)
   context = {      
      'projects': projects
   }
   return render(request, 'portfolio/home.html', context)


def project_detail(request, slug):
   project = get_object_or_404(Project, slug=slug)
   context ={
      'project': project
   }
   return render(request, 'portfolio/project_details.html', context)

def add_project(request):
   return HttpResponse("Add Project")
