# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('creator', models.ForeignKey(related_query_name=b'event', related_name='events', default=0, to=settings.AUTH_USER_MODEL)),
                ('subscribers', models.ManyToManyField(default=0, related_name='subscribers', related_query_name=b'subscriber', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='assignment',
            name='section',
        ),
        migrations.DeleteModel(
            name='Assignment',
        ),
        migrations.RemoveField(
            model_name='section',
            name='students',
        ),
        migrations.RemoveField(
            model_name='section',
            name='teacher',
        ),
        migrations.DeleteModel(
            name='Section',
        ),
    ]
