# Generated by Django 3.2.19 on 2023-06-02 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_question_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='text',
            new_name='question_text',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='text',
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_text',
            field=models.CharField(default='choice text', max_length=400),
        ),
    ]
