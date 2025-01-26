from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.utils import timezone
from blog.models import Post, Category


def index(request):
    post_list = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-created_at')[:5]

    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        if not post.is_published or post.pub_date > timezone.now():
            return HttpResponseNotFound('<h1>404 Post not found</h1>')
        if not post.category.is_published:
            return HttpResponseNotFound('<h1>404 Post not found</h1>')
    except Post.DoesNotExist:
        return HttpResponseNotFound('<h1>404 Post not found</h1>')
    else:
        return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    try:
        category = Category.objects.get(slug=category_slug)
        if not category.is_published:
            return HttpResponseNotFound('<h1>404 Category not found</h1>')
        post_list = Post.objects.filter(
            category=category,
            is_published=True,
            pub_date__lte=timezone.now()
            # published_at__lte=timezone.now()
        ).order_by('-created_at')
    except Category.DoesNotExist:
        return HttpResponseNotFound('<h1>404 Category not found</h1>')
    return render(
        request,
        'blog/category.html',
        {'post_list': post_list, 'category': category}
    )
