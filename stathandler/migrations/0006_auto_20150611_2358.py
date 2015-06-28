# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stathandler', '0005_auto_20150611_2351'),
    ]

    operations = [
        migrations.RenameField(
            model_name='committeestatistic',
            old_name='pointResumes',
            new_name='pointResume',
        ),
    ]
