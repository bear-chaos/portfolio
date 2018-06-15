from django.urls import path
from django.views.generic import TemplateView
from .views import index, education, certificates, skills, my_projects, project_info

app_name = 'rezumeapp'

urlpatterns = [
    path('', index, name='index'),
    path('robots.txt/', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path('education/', education, name='education'),
    path('certificates/', certificates, name='certificates'),
    path('skills/', skills, name='skills'),
    # path('projects/', my_projects, name='projects_list'),
    path('projects/<int:pk>/', project_info, name='project_info'),
    path('projects/<skill>/', my_projects, name='projects_list'),
]
