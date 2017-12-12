from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from home.models import Article


def index(request):
    # return HttpResponse('hello world')

    # 通过id倒叙查询文章
    article_list = Article.objects.filter()[0:4]  # .order_by('-id')
    context = {'title': '首页', 'article_list': article_list}
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
    article_list = Article.objects.filter()
    # 分页对象　
    paginator = Paginator(article_list, 4)
    # 表示当前是第几页
    page = paginator.page(current_page)

    context = {'title': '博客', 'page': page}
    return render(request, 'home/full-width.html', context)


def contact(request):
    """联系方式"""
    context = {'title': '联系'}
    return render(request, 'home/contact.html', context)


def details(request, article_id):
    """文章详细列表"""
    article_list = Article.objects.filter(id=article_id)
    if len(article_list):
        context = {'title': '文章详情', 'article': article_list[0]}
        return render(request, 'home/details.html', context)
    else:
        return HttpResponse('没有此文章，操作有误!自己返回!就是这么傲娇.')
