# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20160603_0030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='benjamin',
        ),
    ]
