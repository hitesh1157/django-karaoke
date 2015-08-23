# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0005_auto_20150823_1521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='performer',
        ),
        migrations.AddField(
            model_name='performer',
            name='song',
            field=models.ForeignKey(default=b'', blank=True, to='songs.Song'),
        ),
    ]
