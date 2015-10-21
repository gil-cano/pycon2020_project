# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('place', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='talk',
            name='track',
            field=models.ForeignKey(default=1, to='talks.Track'),
        ),
    ]
