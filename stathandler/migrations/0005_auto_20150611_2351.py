# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stathandler', '0004_committee_gaposition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='committeestatistic',
            name='funFactDummy',
        ),
        migrations.AddField(
            model_name='committeestatistic',
            name='point_resumes',
            field=models.CharField(default='example', max_length=1000),
            preserve_default=False,
        ),
    ]
