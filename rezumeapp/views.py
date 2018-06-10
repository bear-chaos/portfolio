from django.shortcuts import render, render_to_response, get_object_or_404
from authapp.models import MyUser
from .models import Education, Certificates, Skills, PodSkills, PodPodSkills, Projects
# Create your views here.


def page_404(request, exception):
    user_info = MyUser.objects.get(username='bear_chaos')
    context = {
        'user_info': user_info
    }
    return render(request, '404.html', context, status=404)


def page_500(request):
    user_info = MyUser.objects.get(username='bear_chaos')
    context = {
        'user_info': user_info
    }
    return render(request, '500.html', context, status=500)


# главная
def index(request):
    user_info = MyUser.objects.get(username='bear_chaos')
    context = {
        'user_info': user_info
    }
    return render(request, 'rezumeapp/index.html', context)


# образование
def education(request):
    education_list = Education.objects.all().order_by('date_end')
    user_info = MyUser.objects.get(username='bear_chaos')
    context = {
        'education_list': education_list,
        'user_info': user_info,
    }
    return render(request, 'rezumeapp/education.html', context)


# сертификаты
def certificates(request):
    certificate_list = Certificates.objects.all().order_by('-date_end')
    user_info = MyUser.objects.get(username='bear_chaos')
    context = {
        'certificate_list': certificate_list,
        'user_info': user_info,
    }
    return render(request, 'rezumeapp/certifikate.html', context)


# навыки
def skills(request):
    skills_list = Skills.objects.all()
    podskills_list = PodSkills.objects.all()
    user_info = MyUser.objects.get(username='bear_chaos')
    context = {
        'skills_list': skills_list,
        'podskills_list': podskills_list,
        'user_info': user_info,
    }
    return render(request, 'rezumeapp/skills.html', context)


# проекты
def my_projects(request, skill='all'):
    user_info = MyUser.objects.get(username='bear_chaos')
    if skill != 'all':
        projects_list = Projects.objects.filter(skills__slug=skill).order_by('-date_end')
        if len(projects_list) == 0:
            projects_list = Projects.objects.filter(podskills__slug=skill).order_by('-date_end')
    else:
        projects_list = Projects.objects.all().order_by('-date_end')
    context = {
        'user_info': user_info,
        'projects_list': projects_list,
    }
    return render(request, 'rezumeapp/projects_list.html', context)

# def my_projects(request, skill):
#     user_info = MyUser.objects.get(username='bear_chaos')
#     projects_list = Projects.objects.all().order_by('-date_end')
#     context = {
#         'user_info': user_info,
#         'projects_list': projects_list,
#     }
#     return render(request, 'rezumeapp/projects_list.html', context)


# проект
def project_info(request, pk):
    user_info = MyUser.objects.get(username='bear_chaos')
    project = get_object_or_404(Projects, pk=pk)
    context = {
        'user_info': user_info,
        'project_info': project,
    }
    return render(request, 'rezumeapp/project.html', context)