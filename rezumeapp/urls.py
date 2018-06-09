# from django.conf.urls import handler404
# from django.conf.urls import handler404
from django.urls import path
from .views import index, education, certificates, skills, my_projects, project_info, page_404

app_name = 'rezumeapp'

urlpatterns = [
    path('', index, name='index'),
    path('education/', education, name='education'),
    path('certificates/', certificates, name='certificates'),
    path('skills/', skills, name='skills'),
    # path('projects/', my_projects, name='projects_list'),
    path('projects/<int:pk>/', project_info, name='project_info'),
    path('projects/<skill>/', my_projects, name='projects_list'),
]

# handler404 = 'rezumeapp.views.page_404'
handler404 = page_404