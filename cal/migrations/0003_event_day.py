# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cal', '0002_auto_20141224_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='day',
            field=models.ManyToManyField(default=0, related_name='days', related_query_name=b'day', to='cal.Day'),
            preserve_default=True,
        ),
    ]
