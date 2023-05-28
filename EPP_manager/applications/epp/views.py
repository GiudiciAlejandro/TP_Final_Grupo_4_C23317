from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from datetime import date, timedelta, datetime
from .forms import New_epp, New_epptype
from applications.empleados.models import Worker
from .models import *


def epp_list(request):
    in_stock = [Epp.objects.filter(epp_assigned__isnull=True).count()]
    assigned = [
        Epp.objects.exclude(epp_assigned__isnull=True).count()]
    epps_to_inspect = get_next_to_inspect
    to_inspect=len(epps_to_inspect)
    employe_count = [Worker.objects.count()]
    epps = Epp.objects.all()
    epps_employee =[Epp.objects.exclude(epp_assigned__isnull=True)]
    employees = Worker.objects.all()
    epp_to_expire = get_next_to_expire()
    to_expire = len(epp_to_expire)
    context = {"in_stock": in_stock, "assigned": assigned, "to_expire": to_expire,
               "to_inspect": to_inspect, "employe_count": employe_count, "epps": epps, "employees": employees, "epps_employee":epps_employee, "epps_to_expire": epp_to_expire}
    return render(request, 'epp/resume.html', context)

def get_next_to_inspect():
    # Get EPP list of epp that inspection date in less than 30 days
    epps = Epp.objects.all()
    epps_to_inspect = []
    for insp_date in epps:
        epp_insp_date=insp_date.epp_expire_date
        hoy = date.today()
        time_inspect = ((epp_exp_date - hoy).days)
        if time_expire < 30:
            epps_to_expire.append(insp_date)
    print(epps_to_expire)
    return epps_to_expire


def get_next_to_expire():
    # Get EPP list of epp that expires in less than 30 days
    # TODO Calculate inspection date from insp period from TBL Epp_types
    epps = Epp.objects.all()
    epps_to_expire = []
    for exp_date in epps:
        epp_exp_date=exp_date.epp_expire_date
        hoy = date.today()
        time_expire = ((epp_exp_date - hoy).days)
        if time_expire < 30:
            epps_to_expire.append(exp_date)
    print(epps_to_expire)
    return epps_to_expire

def epp_new(request):
    context = {}
    if request.method == "POST":
        epp_form = New_epp(request.POST)
        # Validations
        if epp_form.is_valid():
            # TODO add next inspection date to DB
            epp_form.save()
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
