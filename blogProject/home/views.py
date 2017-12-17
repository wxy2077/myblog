#!/usr/bin/python3
import markdown
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from comments.forms import CommentForm
from comments.models import Comment
from home.models import Article


def index(request):
    # return HttpResponse('hello world')

    # 通过id倒叙查询文章
    article_list = Article.objects.filter().order_by('-id')[:3]  # .order_by('-id')

    for item in article_list:
        item.content = markdown.markdown(item.content,
                                         extensions=[
                                             'markdown.extensions.extra',
                                             'markdown.extensions.codehilite',
                                             'markdown.extensions.toc',
                                         ])

    context = {'title': '首页', 'article_list': article_list, 'show_right': True}
    return render(request, 'home/index.html', context)


def about(request):
    context = {'title': '关于'}
    return render(request, 'home/about.html', context)


def full(request, current_page):
    """

    :param request:
    :param current_page: 当前页
    :return:
    """
    article_list = Article.objects.filter().order_by('-id')
    # 分页对象　
    paginator = Paginator(article_list, 4)
    # 表示当前是第几页
    page = paginator.page(current_page)

    for item in page:
        item.content = markdown.markdown(item.content,
                                         extensions=[
                                             'markdown.extensions.extra',
                                             'markdown.extensions.codehilite',
                                             'markdown.extensions.toc',
                                         ])

    context = {'title': '博客', 'page': page}
    return render(request, 'home/full-width.html', context)


def contact(request):
    """联系方式"""
    context = {'title': '联系'}
    return render(request, 'home/contact.html', context)


def details(request, article_id):
    """文章详细列表"""
    article = get_object_or_404(Article, pk=article_id)
    # 点击量加１
    article.on_click += 1
    article.save()

    article.content = markdown.markdown(article.content,
                                        extensions=[
                                            'markdown.extensions.extra',
                                            'markdown.extensions.codehilite',
                                            'markdown.extensions.toc',
                                        ])
    comment_num = Comment.objects.filter(article=article_id).count()
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comment_list = article.comment_set.all()

    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {'title': '文章详情',
               'article': article,
               'form': form,
               'comment_list': comment_list,
               'comment_num': comment_num,
               'show_right': True,
               }
    return render(request, 'home/details.html', context)
    # else:
    #     return HttpResponse('没有此文章，操作有误!自己返回!就是这么傲娇 :) ')

