# -*-coding:utf8-*-
from django.db import models


# Create your models here.
class Category(models.Model):
    """
    分类名
    """
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "Category"


class Tag(models.Model):
    """
    标签
    """
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "Tag"


class Article(models.Model):
    """
    文章
    """

    title = models.CharField(max_length=100)
    # 文章简介   blank=True 表示可以不写 没有的话　　此字段必须要有值
    excerpt = models.CharField(max_length=200, blank=True)
    content = models.TextField()

    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()  # 修改时间
    # 分类外键
    category = models.ForeignKey(Category)
    # 多对多　文章和标签
    tags = models.ManyToManyField(Tag, blank=True)

    # 元类重命名
    class Meta:
        db_table = "Article"


