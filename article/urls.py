from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.all_article_list, name='article'),
    path('create/', views.article_create_form, name='create'),
    path('article_detail/<slug:slug>/', views.article_detail_view, name='details'),
    path('article-search/', views.article_search_view, name='search'),
]
