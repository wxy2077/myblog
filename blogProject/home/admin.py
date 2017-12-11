from django.contrib import admin


# Register your models here.
from home.models import Article


class ArticleAdmin(admin.ModelAdmin):
    # 页面中显示的选项
    list_display = ['id', 'title', 'excerpt', 'content', 'create_time',
                    'modified_time',]
    # 每页显示的条数
    list_per_page = 10


admin.site.register(Article, ArticleAdmin)

