# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stathandler', '0002_committee_committeestats'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommitteeStatistic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('funFactDummy', models.TextField()),
                ('committee', models.ForeignKey(to='stathandler.Committee')),
            ],
        ),
        migrations.RemoveField(
            model_name='committeestats',
            name='committee',
        ),
        migrations.DeleteModel(
            name='CommitteeStats',
        ),
    ]
