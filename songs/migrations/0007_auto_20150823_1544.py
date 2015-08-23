# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0006_auto_20150823_1541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='performer',
            name='song',
        ),
        migrations.AddField(
            model_name='song',
            name='performer',
            field=models.ForeignKey(default=b'', blank=True, to='songs.Performer'),
        ),
    ]
