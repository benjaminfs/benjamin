# coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from category.models import Category


class Article(models.Model):
    STATUS_CHOICES = (
            ('d', '草稿'),
            ('p', '发表'),
    )  # 存为草稿或者发表
    ARTICLE_STATUS = (
            (0, u'普通'),
            (1, u'精华')
    )  # 将文章设置为普通或者加精
    owner = models.ForeignKey(User, verbose_name="作者")
    title = models.CharField(u'标题', max_length=100)
    content = models.TextField(u'内容')
    article_url = models.URLField(u'链接', max_length=200)  # 设置文章所指向淘宝的链接
    status = models.CharField(u'文章状态', max_length=5, choices=STATUS_CHOICES)
    article_status = models.IntegerField(u'设置精华／普通', choices=ARTICLE_STATUS)
    # 注意status和article_status的隶属关系，article_status应隶属于status，因为只有发表后的文章
    # 才有　普通　或者　精华　的状态
    abstract = models.CharField(u'摘要', max_length=60, help_text=u"可选，若不填则默认摘取正文的钱６０个字符")
    views = models.PositiveIntegerField(u'浏览量', default=0)
    likes = models.PositiveIntegerField(u"点赞", default=0)
    transmits = models.PositiveIntegerField(u"转发量", default=0)
    topped = models.BooleanField(u'置顶', default=False)
    article_category = models.ForeignKey(Category, verbose_name="分类", null=True, on_delete=models.SET_NULL)
    create_timestamp = models.DateTimeField(u'时间戳', auto_now_add=True)
    last_update_timestamp = models.DateTimeField(u'更新时间戳', auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta():
        verbose_name = u'文章'
        verbose_name_plural = u'文章'
