from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Index Page")

#se concatena el username que se solicita
def hello(request, username):
    return HttpResponse("Hello %s" %username)

def about(request):
    return HttpResponse("About")

def perro(request):
    return HttpResponse("Hola Perro")