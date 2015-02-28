# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sweshare', '0002_auto_20150228_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='edge',
            name='node',
        ),
        migrations.DeleteModel(
            name='Edge',
        ),
        migrations.AddField(
            model_name='node',
            name='node_name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='node',
            name='node_text',
            field=models.CharField(max_length=3000),
            preserve_default=True,
        ),
    ]
