from django.urls import path 
from . import views

urlpatterns = [
    path('hello', views.index, name="hello"),
    path('welcome', views.welcome, name="welcome"),
    path('about', views.about, name="about")
]