from django.urls import path
from .views import home_page, news_detail, category_form, news_form

urlpatterns = [
    path('', home_page, name='home-page'),
    path('news/<int:news_id>/', news_detail, name='news-details-page'),
    path('categories/', category_form, name='categories-form'),
    path('news/', news_form, name='news-form'),

]
