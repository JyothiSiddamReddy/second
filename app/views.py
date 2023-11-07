from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def kiran(request):
    return HttpResponse('<h1>Hello</h1>')
