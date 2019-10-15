from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name="root"),
    path('index', views.index, name="index"),
    path('hello', views.index, name="hello"),
    path('welcome', views.welcome, name="welcome"),
    path('about', views.about, name="about")
]