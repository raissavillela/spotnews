from django.shortcuts import render, get_object_or_404
from .models import News


def index(request):
    news_list = News.objects.all()
    return render(request, 'index.html', {'news_list': news_list})


def news_detail(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news_detail.html', {'news_item': news_item})


def home_page(request):
    news_list = News.objects.all()
    return render(request, 'home.html', {'news_list': news_list})
