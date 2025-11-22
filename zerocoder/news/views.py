from django.shortcuts import render
from .models import New_post

# Create your views here.
def home(request):
    news = New_post.objects.all()
    return render(request, 'news/news.html', {'news': news})

