from django.shortcuts import render, HttpResponse
from service1 import views as v1

# Create your views here.

def index(request):
    return HttpResponse('Hello, World!  —— from service2')

def number(request):
    num = v1.get_number()
    return HttpResponse(num)