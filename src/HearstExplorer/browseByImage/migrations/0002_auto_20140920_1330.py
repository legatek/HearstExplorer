# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('browseByImage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artifact',
            name='production_date_earliest',
            field=models.DateTimeField(verbose_name=b'Earliest production date'),
        ),
        migrations.AlterField(
            model_name='artifact',
            name='production_date_latest',
            field=models.DateTimeField(verbose_name=b'Latest production date'),
        ),
    ]
