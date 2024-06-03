# Generated by Django 5.0.1 on 2024-01-04 13:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0002_rename_course_id_content_course'),
        ('courses', '0002_rename_instructor_id_course_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='courses.course'),
        ),
    ]