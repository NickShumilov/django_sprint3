from django.shortcuts import render
from django.http import HttpResponseNotFound


def index(request):
    template = 'blog/index.html'
    context = {'index': posts[::-1]}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    try:
        context = {'post': posts[id]}
    except IndexError:
        return HttpResponseNotFound('<h1>404 Page not found</h1>')
    else:
        return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    context = {'category_slug': category_slug}
    return render(request, template, context)
