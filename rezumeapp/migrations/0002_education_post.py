# Generated by Django 2.0.4 on 2018-05-18 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rezumeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='post',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Должность'),
        ),
    ]
