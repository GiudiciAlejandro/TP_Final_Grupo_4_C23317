from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request,'index/index.html' )


def login(request):
    return render(request,'index/login.html' )
