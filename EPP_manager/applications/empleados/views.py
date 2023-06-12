from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from .form import Employee_form, Company_form
from .models import *
from datetime import datetime
from applications.epp.forms import Epp


# Create your views here.

@login_required
def employee_lits(request):
    # Show a list of all employees names and surname
    # Clicking in one employee open employee_details page
    context = {}
    employees = Worker.objects.all()
    epp_list= Epp.objects.exclude(epp_assigned__isnull=True)
    list_epp = []
    for empl in employees:
        list_epp_empl = []
        for epp in epp_list:
            if epp.epp_assigned == empl:
                list_epp_empl.append(epp)
        list_epp.append({empl:list_epp_empl}) # Create a list with a dict with a employee data and associated epps
    #context["empleados"] = employees
    #context["epps"] = epp_list
    context['empleados'] = list_epp
    return render(request, 'employee/employee_list.html', context)


@login_required
def employee_details(request, id):
    # Show details for specific employee
    empl = get_object_or_404(Worker,id=id)
    empl_epp = Epp.objects.filter(epp_assigned=empl.id)
    context={"empl_epp":empl_epp, "empl":empl}
    print(empl_epp)
    return render(request, 'employee/employee_details.html', context)
    

@login_required
def employee_update(request, id):
    empl = Worker.objects.get(id=id)
    form_empl = Employee_form(request.POST or None, instance=empl)
    if form_empl.is_valid():
        form_empl.save()
        return redirect("/empleados/employee_list/")
    context={"empl":empl, "form_new_employee":form_empl }
    return render(request, 'employee/update_employee.html', context)



@login_required
def employee_new(request):
    # Show the form to load a new employee
    context = {}
    if request.method == "POST":
        employee_new_form = Employee_form(request.POST)
        # Validaciones
        if employee_new_form.is_valid():
            # Get data from form
            wname = employee_new_form.cleaned_data["worker_name"]
            wsname = employee_new_form.cleaned_data["worker_surname"]
            wcompany = employee_new_form.cleaned_data["worker_company"]
            wnationality = employee_new_form.cleaned_data["worker_nationality"]
            wdoctype = employee_new_form.cleaned_data["worker_doc_type"]
            wdoc_n = employee_new_form.cleaned_data["worker_doc_n"]
            wcomments = employee_new_form.cleaned_data["worker_comments"]
            wemail = employee_new_form.cleaned_data["worker_email"]
            wbirthday = employee_new_form.cleaned_data["worker_birthday"]
            wcertif=employee_new_form.cleaned_data["worker_certifications"]
            
            # Fill table
            # Create new instance of model Worker
            new_employee = Worker(
                worker_name=wname,
                worker_surname=wsname,
                worker_company=wcompany,
                worker_nationality=wnationality,
                worker_doc_type=wdoctype,
                worker_doc_n=wdoc_n,
                worker_birthday = wbirthday,
                worker_email = wemail,
                worker_comments=wcomments,
                worker_state=True,
                worker_certifications=wcertif,
            )
            new_employee.save()
            messages.add_message(
                request, messages.SUCCESS, 'Se han cargado correctamente los datos del nuevo empleado')
            return redirect('employee_new')
        else:
            messages.error(
                request, 'Error al cargar el empleado, por favor revise los datos e intenta nuevamente')
    else:
        employee_new_form = Employee_form()
    context = {'form_new_employee': employee_new_form}
    return render(request, 'employee/employee_new.html', context)



@login_required
def companies_list(request):
    # Show a list of all companies
    context = {}
    companies_list = Company.objects.all()
    context["company"] = companies_list

    return render(request, 'employee/company_list.html', context)



@login_required
def company_new(request):
    # Show the form to load a new employee
    if request.method == "POST":
        company_new_form = Company_form(request.POST)
        # Validaciones
        if company_new_form.is_valid():
            # Get data from form
            cname = company_new_form.cleaned_data["name"]
            cdescript = company_new_form.cleaned_data["description"]
            caddress = company_new_form.cleaned_data["address"]
                        
            # Fill table
            # Create new instance of model Company
            new_company = Company(
                company_name=cname,
                company_descript=cdescript,
                company_address=caddress,
            )
            new_company.save()
            messages.add_message(
                request, messages.SUCCESS, 'Se han cargado correctamente los datos de la nueva empresa')
            return redirect('companies_list')
        else:
            messages.error(
                request, 'Error al cargar el empleado, por favor revise los datos e intenta nuevamente')
    else:
        company_new_form = Company_form()
    context = {'form_new_company': company_new_form}
    return render(request, 'employee/company_new.html', context)


@login_required
def certification(request):
    if request.method == "POST":
        certif_new_form = Certification_form(request.POST)
        if certif_new_form.is_valid():
            certif_new_form.save()
            return redirect('certification_new')
        else:  
            certif_new_form = Certification_form()
        context = {'certif_new_form': certif_new_form}
        return render(request, 'employee/certif_new.html', context)