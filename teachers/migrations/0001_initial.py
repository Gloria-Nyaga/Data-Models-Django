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
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_age', models.IntegerField()),
                ('teacher_name', models.CharField(max_length=20)),
                ('teacher_id', models.IntegerField()),
                ('teacher_course', models.CharField(max_length=20)),
                ('teacher_class', models.CharField(max_length=20)),
                ('teacher_description', models.CharField(max_length=20)),
                ('teacher_occupation', models.CharField(max_length=20)),
                ('teacher_salary', models.IntegerField()),
                ('teacher_hobby', models.CharField(max_length=20)),
                ('teacher_gender', models.CharField(max_length=20)),
                ('students_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='students.students')),
            ],
        ),
    ]
