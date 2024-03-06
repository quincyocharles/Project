from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


def home(request):
    all_posts = Post.objects.all()
    return render(request, 'home.html', {'all_posts': all_posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {'post': post}
    return render(request, 'post_detail.html', context)


def contact(request):
    return render(request, 'contact.html', {})
