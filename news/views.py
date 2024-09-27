from django.shortcuts import render,  get_object_or_404
from .models import News


def home_page(request):
    news_list = News.objects.all()
    return render(request, 'home.html', {'news_list': news_list})


def news_details(request, id):
    news_item = get_object_or_404(News, pk=id)
    return render(request, 'news_details.html', {'news_item': news_item})
