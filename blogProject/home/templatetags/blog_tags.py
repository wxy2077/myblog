#!/usr/bin/python3
# -*- coding:utf-8 -*-
# 自定义模板语言
from django import template

from home.models import Article, Category, Tag

register = template.Library()


@register.simple_tag()  # 注册
def get_recent_article(num=5):
    """
    获取最新的文章
    :param num:  默认返回5条数据
    :return:
    """
    return Article.objects.all().order_by('-create_time')[:num]


@register.simple_tag
def archives():
    """
    按月份归档
    :return:
    """
    return Article.objects.dates('create_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    """
    获取分类
    :return:
    """
    return Category.objects.all()


@register.simple_tag
def get_tags():
    """
    获取所有的分类
    :return:
    """
    return Tag.objects.all()
