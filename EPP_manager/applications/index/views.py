from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth import logout
from django.urls import reverse
from .forms import Logeo, Contact_form


# Create your views here.

def index(request):
    return render(request,'index/index.html' )


def login(request):
    if request.method == "POST":
        logeo_form=Logeo(request.POST)
        # Validaciones
        if logeo_form.is_valid():
            return redirect("/epp/epp_list")
    else:
        logeo_form=Logeo()
    context= {'form_logeo': logeo_form}
    return render(request,'index/login.html' , context)
        
        
def logout_v(request):
    logout(request)
    return redirect('/index/login')


def contact(request):
    if request.method == "POST":
        contact=Contact_form(request.POST)
        # Validaciones
        if contact.is_valid():
            messages.add_message(request, messages.SUCCESS, 'El mensaje fue enviado correctamente, te conestaremos a la brevedad')        
            return redirect('contact')
        else:
            messages.error(request, 'Error al enviar el mensaje, por favor revisa los datos e intenta nuevamente')
    else:
        contact=Contact_form()
    context= {'contact': contact}
    return render(request,'index/contact.html' , context)
    