from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from .forms import logeo


# Create your views here.

def index(request):
    return render(request,'index/index.html' )


def login(request):
    if request.method == "POST":
        logeo_form=logeo(request.POST)
        # Validaciones
        if logeo_form.is_valid():
            return redirect("/empleados/employee_details/ale")
    else:
        logeo_form=logeo()
    context= {'form_logeo': logeo_form}
    return render(request,'index/login.html' , context)
        
        

    
       
