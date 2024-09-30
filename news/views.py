from django.shortcuts import redirect, render, get_object_or_404
from news.serializers import CategorySerializer, UserSerializer, NewsSerializer
from .models import Category, News, User
from .forms import CategoryForm, NewsForm
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


def index(request):
    news_list = News.objects.all()
    return render(request, 'index.html', {'news_list': news_list})


def news_detail(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news_details.html', {'news': news_item})


def home_page(request):
    news_list = News.objects.all()
    return render(request, 'home.html', {'news_list': news_list})


def category_form(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = CategoryForm()

    return render(request, 'categories_form.html', {'form': form})


def news_form(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = NewsForm()
    return render(request, 'news_form.html', {'form': form})


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)