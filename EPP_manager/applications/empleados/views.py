from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.contrib import messages
from .form import Employee_form
from .models import Worker, Countries, Company, Doc_types
from datetime import datetime

# Create your views here.


def employee_lits(request):
    # Show a list of all employees names and surname
    # Clicking in one employee open employee_details page
    context = {}
    employees = Worker.objects.all()
    epp_list=[]
    context["empleados"] = employees

    """epp_1 = [{'type': 'Casco', 'serial_number': 'csc1234', 'manufacturer': 'MSA', 'asign_date': '12-4-2022'}, {'type': 'Anteojos', 'serial_number': 'antdd53234', 'manufacturer': 'North', 'asign_date': '30-1-2021'},
             {'type': 'Zapatos', 'serial_number': 'boots1234', 'manufacturer': 'Honeywell', 'asign_date': '2-8-2009'}]"""

    context["epps"]= epp_list
    return render(request, 'employee/employee_list.html', context)
    pass


def employee_details(request, employee):
    # Show details for specific employee
    # If logged user is admin, it will show a menu to manage employee :
    # delete employee
    # assign EPP
    # deasign EPP
    # go to EPP inspection page
    # If logged user is employee, only have the option to ask for a new EPP or report a damaged EPP
    employee_1 = {
        'first_name': 'Pedro',
        'last_name': 'Del Cerro',
        'age': 35,
        'nacionality': 'Argentino',
        'company': 'company1',
        'document_type': 'passport',
        'document_number': '123456789',
        'email': 'ale@gmail.com',
        'status': 'Active',
        'coment': 'Perosna medio loca',
    }

    epp_1 = [{'type': 'Casco', 'serial_number': 'csc1234', 'manufacturer': 'MSA', 'asign_date': '12-4-2022'}, {'type': 'Anteojos', 'serial_number': 'antdd53234', 'manufacturer': 'North', 'asign_date': '30-1-2021'},
             {'type': 'Zapatos', 'serial_number': 'boots1234', 'manufacturer': 'Honeywell', 'asign_date': '2-8-2009'}]
    
    context = {"empleado": employee_1,
               "epps": epp_1}
    return render(request, 'employee/employee_details.html', context)


def employee_new(request):
    # Show the form to load a new employee
    if request.method == "POST":
        employee_new_form = Employee_form(request.POST)
        # Validaciones
        if employee_new_form.is_valid():
            # Get data from form
            wname = employee_new_form.cleaned_data["name"]
            wsname = employee_new_form.cleaned_data["surname"]
            wcompany = employee_new_form.cleaned_data["company"]
            wnationality = employee_new_form.cleaned_data["nacionality"]
            wdoctype = employee_new_form.cleaned_data["document_type"]
            wdoc_n = employee_new_form.cleaned_data["document_N"]
            wcomments = employee_new_form.cleaned_data["comments"]
            wemail = employee_new_form.cleaned_data["email"]
            wbirthday = employee_new_form.cleaned_data["birthday"]
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
                worker_created=datetime.now()
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
