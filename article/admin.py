# coding:utf-8
from django.contrib import admin
from models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'abstract', 'owner', 'create_timestamp', 'last_update_timestamp')
    list_filter = ('views', 'likes')
    # actions = ['make_category']

    # def makecategory(modeladmin, queryset, request):
    #  for a in queryset:
    # a.status = 1
    # a.save()
    # makestatus.short_description = u"小编推荐"
admin.site.register(Article, ArticleAdmin)
