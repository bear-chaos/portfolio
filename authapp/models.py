from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.
SEX_USER = (
    ('men', 'Мужской'),
    ('women', 'Женский'),
)

MARITAL_STATUS = (
    ('is_married', 'Женат'),
    ('married', 'Замужем'),
    ('single', 'Холост'),
    ('no_married', 'Не замужем'),
)


class MyUser(AbstractUser):
    patronymic = models.CharField(max_length=30, verbose_name='Отчество', blank=True)
    birthday = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    phone1 = models.CharField(max_length=15, verbose_name='Телефон (осн.)', blank=True)
    phone2 = models.CharField(max_length=15, verbose_name='Телефон (доп.)', blank=True)
    skype = models.CharField(max_length=15, verbose_name='Skype', blank=True)
    telegram = models.CharField(max_length=15, verbose_name='Telegram', blank=True)
    avatar = models.ImageField(verbose_name='Аватарка', upload_to='user_avatar', blank=True)
    post = models.CharField(verbose_name='Должность', max_length=100)
    sity = models.CharField(verbose_name='Город', max_length=20)
    sex = models.CharField(verbose_name='Пол', max_length=10, blank=True, choices=SEX_USER)
    marital_status = models.CharField(verbose_name='Сем. статус', max_length=20, blank=True, choices=MARITAL_STATUS)

    def __str__(self):
        return self.username

    def fio(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.patronymic

    def fi(self):
        return self.last_name + ' ' + self.first_name

    def age(self):
        today = datetime.today()
        age = today.year - self.birthday.year
        if today.month < self.birthday.month:
            age -= 1
        elif today.month == self.birthday.today and today.day < self.birthday.day:
            age -= 1
        return str(age)

    def get_marital_status(self):
        return self.get_marital_status_display()