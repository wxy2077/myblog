from django.contrib import admin

# Register your models here.
from home.models import Article, Category, Tag


class ArticleAdmin(admin.ModelAdmin):
    # 页面中显示的选项
    list_display = ['id', 'title', 'excerpt', 'content', 'create_time',
                    'modified_time',]
    # 每页显示的条数
    list_per_page = 10


class CategoryAdmin(admin.ModelAdmin):
    """分类"""
    list_display = ['name']


class TagAdmin(admin.ModelAdmin):
    """标签"""
    list_display = ['name']


# 注册
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
