# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_remove_article_benjamin'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='benjamin',
            field=models.CharField(default=datetime.datetime(2016, 6, 3, 0, 45, 46, 195695), max_length=200),
            preserve_default=False,
        ),
    ]
