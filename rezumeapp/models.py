from django.db import models
from django.template.defaultfilters import slugify



TYPE_EDUCATION = (
    ('secondary', 'Среднее'),
    ('higher', 'Высшее'),
    ('additional', 'Дополнительное'),
)


# Create your models here.
# образование
class Education(models.Model):
    name_institute = models.CharField(max_length=200, verbose_name='Название уч.заведения')
    department = models.CharField(max_length=100, verbose_name='Факультет')
    specialty = models.CharField(max_length=200, verbose_name='Специальность')
    post = models.CharField(max_length=200, verbose_name='Должность', default='', blank=True)
    date_begin = models.DateField(verbose_name='Дата начала')
    date_end = models.DateField(verbose_name='Дата окончания', null=True, blank=True)
    type = models.CharField(max_length=30, verbose_name='Тип образования', choices=TYPE_EDUCATION)
    image = models.ImageField(verbose_name='Изображение диплома', upload_to='education', blank=True)
    image_descr = models.CharField(max_length=100, default='Диплом', blank=True)
    is_active = models.BooleanField(default=False, verbose_name='Удален')

    def __str__(self):
        return self.name_institute

    def get_type_ed(self):
        return self.get_type_display()


# сертификаты
class Certificates(models.Model):
    name = models.CharField(max_length=200, verbose_name='Наименование')
    name_institute = models.CharField(max_length=200, verbose_name='Название уч.заведения')
    description = models.TextField(verbose_name='Описание')
    date_end = models.DateField(verbose_name='Дата получения', null=True, blank=True)
    image = models.ImageField(verbose_name='Изображение сертификата', upload_to='certificates', blank=True)
    image_descr = models.CharField(max_length=100, default='Сертификат', blank=True)
    file = models.FileField(verbose_name='Файл сертификата', blank=True, upload_to='certificates')
    is_active = models.BooleanField(default=False, verbose_name='Удален')

    def __str__(self):
        return self.name


# навыки
class Skills(models.Model):
    name = models.CharField(max_length=250, unique=True, verbose_name='Наименование')
    slug = models.SlugField(max_length=50, blank=True, verbose_name='Slug')
    # slug = models.CharField(max_length=50, unique=True)
    skills_link = models.BooleanField(default=False, verbose_name='Является ли ссылкой')
    is_active = models.BooleanField(default=False, verbose_name='Удален')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save()

    def __str__(self):
        return self.name + ' (' + self.slug + ')'




class PodSkills(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Наименование')
    slug = models.SlugField(blank=True, verbose_name='Slug')
    skills = models.ForeignKey(Skills, on_delete=models.CASCADE, verbose_name='Основной навык')
    is_active = models.BooleanField(default=False, verbose_name='Удален')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save()

    def __str__(self):
        return self.name + ' (' + self.slug + ' - ' + self.skills.name + ')'

    def get_len_podpodskills(self):
        list_podskills = PodPodSkills.objects.filter(podskills=self.pk)
        return len(list_podskills)

    def get_podpodskills(self):
        list_podpodskills = PodPodSkills.objects.filter(podskills=self.pk)
        return list_podpodskills


class PodPodSkills(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(blank=True)
    podskills = models.ForeignKey(PodSkills, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save()

    def __str__(self):
        return self.name + ' (' + self.slug + ' - ' + self.podskills.name + ')'


# проекты
class Projects(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    date_end = models.DateField(verbose_name='Дата окончания', null=True, blank=True)
    img_preview = models.ImageField(verbose_name='Картинка (превью)', upload_to='projects')
    img_preview_descr = models.CharField(max_length=100, default='preview', blank=True)
    img_1 = models.ImageField(verbose_name='Картинка 1', upload_to='projects', blank=True)
    img_1_descr = models.CharField(max_length=100, default='Картинка 1', blank=True)
    img_2 = models.ImageField(verbose_name='Картинка 2', upload_to='projects', blank=True)
    img_2_descr = models.CharField(max_length=100, default='Картинка 2', blank=True)
    img_3 = models.ImageField(verbose_name='Картинка 3', upload_to='projects', blank=True)
    img_3_descr = models.CharField(max_length=100, default='Картинка 3', blank=True)
    img_4 = models.ImageField(verbose_name='Картинка 4', upload_to='projects', blank=True)
    img_4_descr = models.CharField(max_length=100, default='Картинка 4', blank=True)
    file = models.FileField(verbose_name='Файл проекта', upload_to='projects', blank=True)
    link = models.CharField(max_length=250, verbose_name='Ссылка на проект', blank=True)
    skills = models.ManyToManyField(PodSkills, blank=True)
    podskills = models.ManyToManyField(PodPodSkills, blank=True)
    is_active = models.BooleanField(default=False, verbose_name='Удален')

    def __str__(self):
        return self.name