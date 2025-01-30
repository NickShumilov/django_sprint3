from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.utils import timezone
from blog.models import Post, Category

Max_Posts_on_page = 5


def index(request):
    post_list = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-created_at')[:Max_Posts_on_page]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    post = get_object_or_404(
        Post,
        is_published=True,
        id=post_id
    )
    if not post.category.is_published or post.pub_date > timezone.now():
        raise Http404('<h1>404 Post not found</h1>')
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        is_published=True,
        slug=category_slug
    )
    post_list = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-created_at')
    return render(
        request,
        'blog/category.html',
        {'post_list': post_list, 'category': category}
    )
