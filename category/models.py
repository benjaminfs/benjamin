# coding:utf-8
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(u'类名', max_length=50)
    owner = models.ForeignKey(User, verbose_name=u'管理员')
    create_timestamp = models.DateTimeField(u'时间戳', auto_now_add=True)
    last_update_timestamp = models.DateTimeField(u'更新时间戳', auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta():
        verbose_name = u'文章分类'
        verbose_name_plural = u'文章分类'
