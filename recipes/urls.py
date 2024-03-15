from django.urls import path
from . import views


app_name = 'recipe'
urlpatterns = [
    path('', views.recipe_list_view, name='recipe-list'),
    path('create/', views.recipe_create_view, name='create'),
    path('detail/<int:value_from_url>/', views.recipe_detail_view, name='detail'),
    path('update/<int:value_from_url>/', views.recipe_update_views, name='update'),
    path('recipes/<int:value_from_url>/', views.recipe_delete_view, name='delete'),
]
