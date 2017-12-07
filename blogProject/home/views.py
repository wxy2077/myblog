from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    """
    主页
    :param request:
    :return:
    """
    # return HttpResponse('hello world')
    context = {'title': '首页'}
    return render(request, 'home/index.html', context)


def about(request):
    """
    关于页面的
    :param request:
    :return:
    """
    context = {'title': '关于'}
    return render(request, 'home/about.html', context)


def full(request):
    """
    博客文章页面
    :param request:
    :return:
    """
    context = {'title': '博客'}
    return render(request, 'home/full-width.html', context)


def contact(request):
    """联系方式"""
    context = {'title': '联系'}
    return render(request, 'home/contact.html', context)
