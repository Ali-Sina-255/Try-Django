from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_article_list, name='article'),
    path('create/', views.article_create_form, name='article'),
    path('article_detail/<slug:slug>/', views.article_detail_view, name='article_details'),
    path('article-search/', views.article_search_view, name='search'),
]
