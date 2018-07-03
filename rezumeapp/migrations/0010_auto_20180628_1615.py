# Generated by Django 2.0.5 on 2018-06-28 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rezumeapp', '0009_auto_20180520_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificates',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Удален'),
        ),
        migrations.AddField(
            model_name='education',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Удален'),
        ),
        migrations.AddField(
            model_name='podskills',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Удален'),
        ),
        migrations.AddField(
            model_name='projects',
            name='img_1_descr',
            field=models.CharField(blank=True, default='Картинка 1', max_length=100),
        ),
        migrations.AddField(
            model_name='projects',
            name='img_2_descr',
            field=models.CharField(blank=True, default='Картинка 2', max_length=100),
        ),
        migrations.AddField(
            model_name='projects',
            name='img_3_descr',
            field=models.CharField(blank=True, default='Картинка 3', max_length=100),
        ),
        migrations.AddField(
            model_name='projects',
            name='img_4_descr',
            field=models.CharField(blank=True, default='Картинка 4', max_length=100),
        ),
        migrations.AddField(
            model_name='projects',
            name='img_preview_descr',
            field=models.CharField(blank=True, default='preview', max_length=100),
        ),
        migrations.AddField(
            model_name='projects',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Удален'),
        ),
        migrations.AddField(
            model_name='skills',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Удален'),
        ),
        migrations.AlterField(
            model_name='podskills',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='podskills',
            name='skills',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rezumeapp.Skills', verbose_name='Основной навык'),
        ),
        migrations.AlterField(
            model_name='podskills',
            name='slug',
            field=models.SlugField(blank=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='name',
            field=models.CharField(max_length=250, unique=True, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='skills_link',
            field=models.BooleanField(default=False, verbose_name='Является ли ссылкой'),
        ),
        migrations.AlterField(
            model_name='skills',
            name='slug',
            field=models.SlugField(blank=True, verbose_name='Slug'),
        ),
    ]