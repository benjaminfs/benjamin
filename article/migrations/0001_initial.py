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
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u9898\u76ee')),
                ('content', models.CharField(max_length=500000, verbose_name='\u5185\u5bb9')),
                ('gift_attribute', models.CharField(default=b'smallerthan50', max_length=200, choices=[(b'smallerthan5', '5\u4ee5\u4e0b'), (b'between6and10', '6-10\u4e4b\u95f4'), (b'00000011', '11-20\u4e4b\u95f4'), (b'00000100', '21-30\u4e4b\u95f4'), (b'00000101', '31-40\u4e4b\u95f4'), (b'00001100', '41\u4ee5\u4e0a')])),
                ('gift_url', models.URLField(verbose_name='\u94fe\u63a5')),
                ('status', models.IntegerField(choices=[(0, '\u4e00\u822c'), (1, '\u63a8\u8350')])),
                ('benjamin', models.CharField(max_length=200)),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='\u65f6\u95f4\u6233')),
                ('last_update_timestamp', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4\u6233')),
                ('owner', models.ForeignKey(verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
    ]
