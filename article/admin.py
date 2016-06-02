# coding:utf-8
from django.contrib import admin
from models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'owner', 'create_timestamp', 'last_update_timestamp')
    list_filter = ('gift_attribute', )
    actions = ['make_gift_attribute']

    def makestatus(modeladmin, queryset, request):
        for a in queryset:
            a.status = 1
            a.save()
    makestatus.short_description = u"小编推荐"
admin.site.register(Article, ArticleAdmin)
