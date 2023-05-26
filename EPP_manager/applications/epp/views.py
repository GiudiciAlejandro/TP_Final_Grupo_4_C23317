from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from .forms import New_epp, New_epptype


def epp_list(request):
    in_stock=[]

    context={"in_stock":in_stock, "assigned":assigned,"to_expire":to_expire, "to_inspect":to_inspect,"employees":employees }
    return render(request,'epp/resume.html', context)

def epp_new(request):
    context = {}
    if request.method == "POST":
        epp_form = New_epp(request.POST)
        # Validations
        if epp_form.is_valid():
            epp_form.save()
            messages.add_message(request, messages.SUCCESS, 'El EPP fue cargado correctamente')
            return redirect("/epp/epp_new")
        else:
            messages.add_message(request, messages.ERROR, 'Error al cargar los datos, por favor verifique los mismos e intente nuevamente')
    else:
        epp_form = New_epp()
    context = {'form_epp': epp_form}
    return render(request,'epp/alta_epp.html', context)

    
def epp_type(request):
    if request.method == "POST":
        epptype_form = New_epptype(request.POST)
        # Validations
        if epptype_form.is_valid():
            epptype_form.save()
            messages.add_message(request, messages.SUCCESS, 'El tipo de EPP fue cargado correctamente')
            return redirect("/epp/epp_type")
        else:
            messages.add_message(request, messages.ERROR, 'Error al cargar los datos, por favor verifique los mismos e intente nuevamente')
    else:
        epptype_form = New_epptype()
    context = {'form_epptype': epptype_form}
    return render(request,'epp/alta_EPPtype.html', context)




