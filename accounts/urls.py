from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('', views.login_authentication_form, name='login'),
    path('register/', views.user_registration_form, name='register'),
]
