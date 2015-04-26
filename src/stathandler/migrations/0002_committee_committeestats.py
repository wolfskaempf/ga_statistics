# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stathandler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Committee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('acronym', models.CharField(max_length=10)),
                ('longName', models.CharField(max_length=200)),
                ('topic', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CommitteeStats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('funFactDummy', models.TextField()),
                ('committee', models.ForeignKey(to='stathandler.Committee')),
            ],
        ),
    ]
