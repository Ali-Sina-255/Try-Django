from django.urls import path
from . import views


urlpatterns = [
    path('', views.article_create_view, name='article')
]
