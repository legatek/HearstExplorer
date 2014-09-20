# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artifact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('catalog_object_id', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=2000)),
                ('image_url', models.URLField(max_length=300)),
                ('lat_long', models.CharField(max_length=50)),
                ('production_date', models.CharField(max_length=75)),
                ('production_date_earliest', models.TimeField()),
                ('production_date_latest', models.TimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
