# Generated by Django 5.0.7 on 2024-07-21 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('students_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('code', models.PositiveSmallIntegerField()),
                ('date_of_birth', models.DateField()),
                ('country', models.CharField(max_length=20)),
                ('bio', models.TextField()),
                ('age', models.PositiveSmallIntegerField()),
                ('nextOfKin', models.CharField(max_length=20)),
                ('picture', models.ImageField(upload_to='photos/')),
                ('created_on', models.DateField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
