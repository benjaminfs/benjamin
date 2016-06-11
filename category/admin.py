# coding:utf-8
from django.contrib import admin
from models import Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'create_timestamp', 'last_update_timestamp')
    list_filter = ('name', 'last_update_timestamp')

admin.site.register(Category, CategoryAdmin)
