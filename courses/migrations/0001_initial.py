# Generated by Django 5.0.7 on 2024-07-21 19:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses_name', models.CharField(max_length=20)),
                ('courses_code', models.SmallIntegerField()),
                ('courses_instuctor', models.CharField(max_length=20)),
                ('courses_assignment', models.CharField(max_length=20)),
                ('courses_level', models.CharField(max_length=20)),
                ('courses_department', models.CharField(max_length=20)),
                ('courses_syllabus', models.CharField(max_length=20)),
                ('courses_exams', models.CharField(max_length=20)),
                ('courses_term', models.CharField(max_length=10)),
                ('students_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='students.students')),
            ],
        ),
    ]
