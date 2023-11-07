from django.shortcuts import render
from django.http import HttpResponse
import requests
from rest_framework.response import Response

# Create your views here.

def crossF(request):
    n = requests.get("http://127.0.0.1:8000/num/")
    print("n:", n)
    return HttpResponse(n)
