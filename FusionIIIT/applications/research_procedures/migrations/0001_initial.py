# Generated by Django 3.1.5 on 2024-04-15 23:58

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('globals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pf_no', models.IntegerField()),
                ('details', models.CharField(default=' ', max_length=500)),
                ('date_entry', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResearchProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pf_no', models.IntegerField()),
                ('ptype', models.CharField(default='Research', max_length=100)),
                ('pi', models.CharField(default=' ', max_length=1000)),
                ('co_pi', models.CharField(default=' ', max_length=1500)),
                ('title', models.TextField(default=' ', max_length=5000)),
                ('funding_agency', models.CharField(default=' ', max_length=250, null=True)),
                ('financial_outlay', models.CharField(default=' ', max_length=150, null=True)),
                ('status', models.CharField(choices=[('Awarded', 'Awarded'), ('Submitted', 'Submitted'), ('Ongoing', 'Ongoing'), ('Completed', 'Completed')], max_length=10)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('finish_date', models.DateField(blank=True, null=True)),
                ('date_submission', models.DateField(blank=True, null=True)),
                ('date_entry', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResearchGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('faculty_under_group', models.ManyToManyField(related_name='allfaculty', to=settings.AUTH_USER_MODEL)),
                ('students_under_group', models.ManyToManyField(related_name='allstudents', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patent',
            fields=[
                ('application_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120)),
                ('ipd_form', models.FileField(blank=True, null=True, upload_to='')),
                ('project_details', models.FileField(blank=True, null=True, upload_to='')),
                ('ipd_form_file', models.TextField(blank=True, null=True)),
                ('project_details_file', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Approved', 'Approved'), ('Disapproved', 'Disapproved'), ('Pending', 'Pending')], default='Pending', max_length=20)),
                ('faculty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.extrainfo')),
            ],
        ),
        migrations.CreateModel(
            name='ConsultancyProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pf_no', models.IntegerField()),
                ('consultants', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=1000)),
                ('client', models.CharField(max_length=1000)),
                ('financial_outlay', models.IntegerField()),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('duration', models.CharField(blank=True, max_length=500, null=True)),
                ('date_entry', models.DateField(blank=True, default=datetime.datetime.now, null=True)),
                ('status', models.CharField(blank=True, choices=[('Completed', 'Completed'), ('Submitted', 'Submitted'), ('Ongoing', 'Ongoing')], default='Ongoing', max_length=10, null=True)),
                ('remarks', models.CharField(blank=True, max_length=1000, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]