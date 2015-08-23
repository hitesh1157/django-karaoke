# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0004_auto_20150823_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='length',
            field=models.IntegerField(),
        ),
    ]
