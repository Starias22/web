# Generated by Django 4.1.7 on 2023-03-22 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_remove_course_lastupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.TextField(default='teacher_name'),
            preserve_default=False,
        ),
    ]