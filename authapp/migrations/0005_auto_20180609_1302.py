# Generated by Django 2.0.4 on 2018-06-09 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_auto_20180524_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='skype',
            field=models.CharField(blank=True, max_length=15, verbose_name='Skype'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='telegram',
            field=models.CharField(blank=True, max_length=15, verbose_name='Telegram'),
        ),
    ]