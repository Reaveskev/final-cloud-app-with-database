# Generated by Django 3.1.3 on 2023-06-02 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.CharField(default='question title', max_length=550),
        ),
    ]
