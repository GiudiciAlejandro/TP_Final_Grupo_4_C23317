from django.shortcuts import render
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
            
            #return redirect("index")

    else:
        logeo_form=logeo()



   # return super().method == "POST":
    context= {'form_logeo': logeo_form}
    return render(request,'index/login.html' , context)
        
        

    
       
