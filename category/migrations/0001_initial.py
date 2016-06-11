# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u7c7b\u540d')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='\u65f6\u95f4\u6233')),
                ('last_update_timestamp', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4\u6233')),
                ('owner', models.ForeignKey(verbose_name='\u7ba1\u7406\u5458', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u6587\u7ae0\u5206\u7c7b',
                'verbose_name_plural': '\u6587\u7ae0\u5206\u7c7b',
            },
        ),
    ]
