from django.urls import path
from .views import home_view, project_detail,add_project


urlpatterns = [
   path('', home_view, name="home_view"),
   path('project_detail/<slug:slug>/', project_detail, name="project-detail"),
   path('addproject/', add_project, name="add-project")
]
