from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World of Django")

def welcome(request):
    return HttpResponse("<h1>I'm the Welcome Page</h1>")

def about(request):
    return HttpResponse("<h1>I am Michael :)!</h1>")