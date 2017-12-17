from django.db import models

# Create your models here.

from django.db import models
from django.utils.six import python_2_unicode_compatible


# python_2_unicode_compatible 装饰器用于兼容 Python2
@python_2_unicode_compatible
class Comment(models.Model):
    name = models.CharField(max_length=100, verbose_name='评论人名')

    email = models.EmailField(max_length=255, verbose_name='邮箱')

    url = models.URLField(blank=True)

    text = models.TextField(verbose_name='评论内容')

    created_time = models.DateTimeField(auto_now_add=True)

    article = models.ForeignKey('home.Article')

    def __str__(self):
        return self.text[:20]
