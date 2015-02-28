# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sweshare', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='edge',
            old_name='choice_text',
            new_name='edge_text',
        ),
    ]
