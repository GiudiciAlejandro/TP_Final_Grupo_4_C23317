from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse


def epp_list(request):
    return render(request,'epp/resume.html' )

def epp_new(request):
    pass



