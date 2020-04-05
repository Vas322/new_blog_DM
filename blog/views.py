from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


# Create your views here.
def post_list(request):
    """Вьюха, которая отображает список всех постов"""
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        '-published_date')[:5]
    return render(request, "blog/post_list.html", {'posts': posts})


def post_detail(request, pk):
    """Вьюха для отображения деталей каждого поста"""
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
