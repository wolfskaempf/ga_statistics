# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stathandler', '0007_auto_20150628_2059'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DummyData',
        ),
    ]
