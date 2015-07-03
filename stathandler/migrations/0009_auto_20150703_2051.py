# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stathandler', '0008_delete_dummydata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='committeestatistic',
            name='pointResume',
            field=models.TextField(),
        ),
    ]
