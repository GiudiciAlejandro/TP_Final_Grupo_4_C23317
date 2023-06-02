from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from datetime import date, timedelta, datetime
from .forms import New_epp, New_epptype, New_insp
from applications.empleados.models import Worker
from .models import *


def epp_list(request):
    in_stock_count = [Epp.objects.filter(epp_assigned__isnull=True).count()]
    in_stock = [Epp.objects.filter(epp_assigned__isnull=True)]
    assigned = [Epp.objects.exclude(epp_assigned__isnull=True).count()]
    epps_to_inspect = get_next_to_inspect()
    to_inspect_count=len(epps_to_inspect)
    employe_count = [Worker.objects.count()]
    epps = Epp.objects.all()
    epps_employee =[Epp.objects.exclude(epp_assigned__isnull=True)]
    employees = Worker.objects.all()
    epp_to_expire = get_next_to_expire()
    to_expire = len(epp_to_expire)
    context = {"in_stock_count": in_stock_count, 
                "in_stock": in_stock,
                "assigned": assigned, 
                "to_expire": to_expire,
                "to_inspect_count": to_inspect_count, 
                "epps_to_inspect": epps_to_inspect, 
                "employe_count": employe_count, 
                "epps": epps, 
                "employees": employees, 
                "epps_employee":epps_employee, 
                "epps_to_expire": epp_to_expire}
    return render(request, 'epp/resume.html', context)

def get_next_to_inspect():
    # Get EPP list of epp that inspection date in less than 30 days
    epps = Epp.objects.all()
    epps_to_inspect = []
    for epp in epps:
        epp_insp_date=epp.epp_next_insp_date
        hoy = date.today()
        days_to_inspect= epp_insp_date - hoy
        if (days_to_inspect).days < 30:
            epps_to_inspect.append(epp)
    return epps_to_inspect


def get_next_to_expire():
    # Get EPP list of epp that expires in less than 30 days
    epps = Epp.objects.all()
    epps_to_expire = []
    for exp_date in epps:
        epp_exp_date=exp_date.epp_expire_date
        hoy = date.today()
        time_expire = ((epp_exp_date - hoy).days)
        if time_expire < 30:
            epps_to_expire.append(exp_date)
    return epps_to_expire

def epp_new(request):
    context = {}
    if request.method == "POST":
        epp_form = New_epp(request.POST)
        # Validations
        if epp_form.is_valid():
            nepp_type=epp_form.cleaned_data["epp_type"]
            nepp_serial_n=epp_form.cleaned_data["epp_serial_n"]
            nepp_manufacturer=epp_form.cleaned_data["epp_manufacturer"]
            nepp_expire_date=epp_form.cleaned_data["epp_expire_date"]
            nepp_assigned=epp_form.cleaned_data["epp_assigned"]
            # Calculate next inspection date to insert in table
            epp_insp_days=nepp_type.epp_type_insp_period
            next_insp=(date.today() + timedelta(days=epp_insp_days)) 
            new_epp = Epp(
                epp_type=nepp_type,
                epp_serial_n=nepp_serial_n,
                epp_manufacturer=nepp_manufacturer,
                epp_expire_date=nepp_expire_date,
                epp_assigned=nepp_assigned,
                epp_next_insp_date= next_insp
            )
            new_epp.save()
            messages.add_message(request, messages.SUCCESS,
                                 'El EPP fue cargado correctamente')
            return redirect("/epp/epp_new")
        else:
            messages.add_message(
                request, messages.ERROR, 'Error al cargar los datos, por favor verifique los mismos e intente nuevamente')
    else:
        epp_form = New_epp()
    context = {'form_epp': epp_form}
    return render(request, 'epp/alta_epp.html', context)


def epp_type(request):
    if request.method == "POST":
        epptype_form = New_epptype(request.POST)
        # Validations
        if epptype_form.is_valid():
            epptype_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'El tipo de EPP fue cargado correctamente')
            return redirect("/epp/epp_type")
        else:
            messages.add_message(
                request, messages.ERROR, 'Error al cargar los datos, por favor verifique los mismos e intente nuevamente')
    else:
        epptype_form = New_epptype()
    context = {'form_epptype': epptype_form}
    return render(request, 'epp/alta_EPPtype.html', context)


"""def epp_detail(request, id):
    epp = get_object_or_404(Epp,id=id)
    context={"epp":epp}
    return render(request, 'epp/detail_EPP.html', context)"""


def epp_detail(request,id):
    epp = get_object_or_404(Epp,id=id)
    epp_insp = [Epp_inspections.objects.filter(epp_inps_epp=epp.id)]
    # Calculate next inspection date to insert in table Epp
    epp_insp_days=epp.epp_type.epp_type_insp_period
    epp_next_insp_date=(date.today() + timedelta(days=epp_insp_days)) 
    if request.method == "POST":
        new_insp_form = New_insp(request.POST)
        if new_insp_form.is_valid():
            new_insp_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'El tipo de EPP fue cargado correctamente')
            return redirect("/epp/epp_list")
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error al cargar inspección')
    else:
        new_insp_form = New_insp()
        new_insp_form.epp_insp_date=date.today()
        new_insp_form.fields['epp_inps_epp'].initial = epp.id
    context={"epp":epp, "epp_insp":epp_insp, "new_insp_form":new_insp_form}
    return render(request, 'epp/detail_EPP.html', context)




def epp_update(request, id):
    epp = Epp.objects.get(id=id)
    form_epp = New_epp(request.POST or None, instance=epp)
    if form_epp.is_valid():
        form_epp.save()
        messages.add_message(request, messages.SUCCESS,
                                'El EPP fue actualizado correctamente')
        return redirect("/epp/epp_list")
    context={"epp":epp, "form_epp":form_epp }
    return render(request, 'epp/update_EPP.html', context)


def insp_new(request):
    if request.method == "POST":
        insp_form = New_insp(request.POST)
        # Validations
        if insp_form.is_valid():
            insp_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Se ha guardado correctamente la nueva inspección')
            return redirect("/epp/epp_type")
        else:
            messages.add_message(
                request, messages.ERROR, 'Error al cargar los datos, por favor verifique los mismos e intente nuevamente')
    else:
        insp_form = New_insp()
    context = {'insp_form': insp_form}
    return render(request, 'epp/insp_new.html', context)