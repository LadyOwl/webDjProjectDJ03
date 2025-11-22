from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import New_post

def home(request):
    news = New_post.objects.all().order_by('-pub_date')
    return render(request, 'news/news.html', {'news': news})

@login_required
def create_news(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        short_description = request.POST.get('short_description')
        text = request.POST.get('text')
        new_post = New_post(
            title=title,
            short_description=short_description,
            text=text,
            pub_date=timezone.now(),
            author=request.user
        )
        new_post.save()
        return redirect('news_home')
    return render(request, 'news/create_news.html')

