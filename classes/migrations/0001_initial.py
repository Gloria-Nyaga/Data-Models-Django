# Generated by Django 5.0.7 on 2024-07-21 19:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_time', models.IntegerField()),
                ('class_capacity', models.IntegerField()),
                ('class_name', models.CharField(max_length=20)),
                ('class_lecture', models.CharField(max_length=20)),
                ('class_id', models.IntegerField()),
                ('class_rep', models.CharField(max_length=20)),
                ('class_description', models.TextField()),
                ('class_attendance', models.IntegerField()),
                ('class_activity', models.CharField(max_length=20)),
                ('students_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='students.students')),
            ],
        ),
    ]
