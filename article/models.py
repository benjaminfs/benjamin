# coding:utf-8
from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    ARTICLE_ATTRIBUTE_CHOICES = (
                        ('smallerthan5', u'5以下'),  # 01
                        ('between6and10', u'6-10之间'),  # 02
                        ('00000011', u'11-20之间'),  # 03
                        ('00000100', u'21-30之间'),  # 04
                        ('00000101', u'31-40之间'),  # 05
                        ('00001100', u'41以上'),  # 06
                            )
    owner = models.ForeignKey(User, verbose_name="作者")
    title = models.CharField(u'题目', max_length=100)
    content = models.CharField(u'内容', max_length=500000)
    gift_attribute = models.CharField(choices=ARTICLE_ATTRIBUTE_CHOICES, default='smallerthan50', max_length=200)
    gift_url = models.URLField(u'链接', max_length=200)
    status = models.IntegerField(choices=((0, u'一般'), (1, u'推荐'),))
    benjamin = models.CharField(max_length=200)  # 这是新添加的字段
    create_timestamp = models.DateTimeField(u'时间戳', auto_now_add=True)
    last_update_timestamp = models.DateTimeField(u'更新时间戳', auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta():
        verbose_name = u'文章'
        verbose_name_plural = u'文章'
