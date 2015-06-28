# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stathandler', '0006_auto_20150611_2358'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='committee',
            options={'ordering': ['gaPosition']},
        ),
        migrations.AlterModelOptions(
            name='committeestatistic',
            options={'ordering': ['-pk']},
        ),
    ]
