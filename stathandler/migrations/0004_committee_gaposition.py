# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stathandler', '0003_auto_20150426_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='committee',
            name='gaPosition',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
