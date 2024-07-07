# Generated by Django 5.0.6 on 2024-07-07 07:07

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseEnrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_email', models.CharField(max_length=30)),
                ('user_mobile', models.CharField(max_length=11)),
                ('course_name', models.CharField(max_length=50)),
                ('testimonial', models.CharField(blank=True, max_length=200, null=True)),
                ('course_completion', models.CharField(max_length=1)),
                ('testimonial_status', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'course_enrollments',
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=255)),
                ('testimonial', models.TextField()),
                ('accept', models.BooleanField(default=False)),
                ('action_by', models.CharField(blank=True, max_length=255, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('email', models.ForeignKey(db_column='email_id', on_delete=django.db.models.deletion.CASCADE, related_name='testimonials', to='myapp.registration')),
            ],
        ),
    ]