from django.urls import path
from . import views


urlpatterns = [
    path('', views.article_create_view, name='article'),
    path('article_detail/<int:value_from_url>/', views.article_detail_view, name='article_detail'),
]
