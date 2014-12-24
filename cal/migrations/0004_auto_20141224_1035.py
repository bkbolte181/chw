# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0003_event_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='creator',
            field=models.ForeignKey(related_query_name=b'creator', related_name='creators', default=0, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
