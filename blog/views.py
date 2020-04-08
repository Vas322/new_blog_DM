from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm


# Create your views here.
def post_list(request):
    """Вьюха, которая отображает список всех постов"""
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        '-published_date')
    context = {'posts': posts}
    return render(request, "blog/post_list.html", context)


def post_detail(request, pk):
    """Вьюха для отображения деталей каждого поста"""
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)


def post_new(request):
    """Вьюха для создания нового поста поста"""
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    """Вьюха для редактирования поста"""
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_draft_list(request):
    """Вьюха, которая показывает не опубликованные посты"""
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


def post_publish(request, pk):
    """Вьюха, которая публикует запись"""
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


def post_remove(request, pk):
    """Вьюха, которая удаляет пост"""
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
