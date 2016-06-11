# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('category', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u6807\u9898')),
                ('content', models.TextField(verbose_name='\u5185\u5bb9')),
                ('article_url', models.URLField(verbose_name='\u94fe\u63a5')),
                ('status', models.CharField(max_length=5, verbose_name='\u6587\u7ae0\u72b6\u6001', choices=[(b'd', b'\xe8\x8d\x89\xe7\xa8\xbf'), (b'p', b'\xe5\x8f\x91\xe8\xa1\xa8')])),
                ('article_status', models.IntegerField(verbose_name='\u8bbe\u7f6e\u7cbe\u534e\uff0f\u666e\u901a', choices=[(0, '\u666e\u901a'), (1, '\u7cbe\u534e')])),
                ('abstract', models.CharField(help_text='\u53ef\u9009\uff0c\u82e5\u4e0d\u586b\u5219\u9ed8\u8ba4\u6458\u53d6\u6b63\u6587\u7684\u94b1\uff16\uff10\u4e2a\u5b57\u7b26', max_length=60, verbose_name='\u6458\u8981')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='\u6d4f\u89c8\u91cf')),
                ('likes', models.PositiveIntegerField(default=0, verbose_name='\u70b9\u8d5e')),
                ('transmits', models.PositiveIntegerField(default=0, verbose_name='\u8f6c\u53d1\u91cf')),
                ('topped', models.BooleanField(default=False, verbose_name='\u7f6e\u9876')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True, verbose_name='\u65f6\u95f4\u6233')),
                ('last_update_timestamp', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4\u6233')),
                ('article_category', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb', to='category.Category', null=True)),
                ('owner', models.ForeignKey(verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
    ]
