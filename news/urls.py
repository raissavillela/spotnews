from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home-page'),
    path('news/<int:id>/', views.news_details, name='news-details-page'),
]
