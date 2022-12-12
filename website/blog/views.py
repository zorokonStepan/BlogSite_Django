from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Post


@login_required  # ограничение доступа к профилям для незарегистрированных пользователей
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


@login_required  # ограничение доступа к профилям для незарегистрированных пользователей
def about(request):
    return render(request, 'blog/about.html', {'title': 'О клубе Django'})