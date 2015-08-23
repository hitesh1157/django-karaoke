# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performer',
            name='song',
            field=models.ForeignKey(to='songs.Song', null=True),
        ),
    ]
