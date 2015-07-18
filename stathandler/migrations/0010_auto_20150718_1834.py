# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stathandler', '0009_auto_20150703_2051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='committeestatistic',
            old_name='committee',
            new_name='proposingCommittee',
        ),
    ]
