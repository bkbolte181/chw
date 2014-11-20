# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('email', models.EmailField(help_text=b'Emory Email Address', unique=True, max_length=200, verbose_name=b'email address', error_messages={b'unique': b'A user with that email already exists.'})),
                ('first_name', models.CharField(help_text=b'First Name', max_length=100)),
                ('last_name', models.CharField(help_text=b'Last Name', max_length=100)),
                ('user_type', models.CharField(help_text=b'Student or Teacher', max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'Assignment Name', max_length=100)),
                ('description', models.CharField(help_text=b'Assignment Description', max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enrollment_number', models.CharField(help_text=b'Enrollment Number', max_length=100)),
                ('students', models.ManyToManyField(default=0, related_name='student_sections', related_query_name=b'student_section', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(related_query_name=b'teacher_section', related_name='teacher_sections', default=0, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='assignment',
            name='section',
            field=models.ForeignKey(related_query_name=b'assignment', related_name='assignments', default=0, to='cal.Section'),
            preserve_default=True,
        ),
    ]
