from django.contrib import admin
from .models import Education, Certificates, Skills, PodSkills, PodPodSkills, Projects

# Register your models here.
admin.site.register(Education)
admin.site.register(Certificates)
admin.site.register(Skills)
admin.site.register(PodSkills)
admin.site.register(PodPodSkills)
admin.site.register(Projects)