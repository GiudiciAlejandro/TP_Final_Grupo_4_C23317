from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from .form import BajaEmpleadoForm, Employee

# Create your views here.


def employee_lits(request):
    # Show a list of all employees names and surname
    # Clicking in one employee open employee_details page
    employees=[{
        'first_name': 'Pedro',
        'last_name': 'Del Cerro', 
        'age': 35,
        'nacionality': 'Argentino',
        'company':'company1',
        'document_type':'passport',
        'document_number':'123456789',
        'email':'ale@gmail.com',
        'status': 'Active',
        'linkto': '/empleados/employee_details/Pedro'},
        {
        'first_name': 'Ale',
        'last_name': 'Del Cerro', 
        'age': 35,
        'nacionality': 'Argentino',
        'company':'company1',
        'document_type':'passport',
        'document_number':'123456789',
        'email':'ale@gmail.com',
        'status': 'Active',
        'linkto': '/empleados/employee_details/Ale'}
    ]
    
    epp_1=[{'type':'Casco', 'serial_number':'csc1234', 'manufacturer':'MSA', 'asign_date':'12-4-2022'},{'type':'Anteojos', 'serial_number':'antdd53234', 'manufacturer':'North', 'asign_date':'30-1-2021'},
    {'type':'Zapatos', 'serial_number':'boots1234', 'manufacturer':'Honeywell', 'asign_date':'2-8-2009'}]
    

    context={"empleados":employees, 
             "epps":epp_1}
    return render(request,'employee/employee_list.html', context )
    pass


def employee_details(request, employee):
    # Show details for specific employee
    # If logged user is admin, it will show a menu to manage employee :
        # delete employee
        # assign EPP
        # deasign EPP
        # go to EPP inspection page
    # If logged user is employee, only have the option to ask for a new EPP or report a damaged EPP
    employee_1={
        'first_name': 'Pedro',
        'last_name': 'Del Cerro', 
        'age': 35,
        'nacionality': 'Argentino',
        'company':'company1',
        'document_type':'passport',
        'document_number':'123456789',
        'email':'ale@gmail.com',
        'status': 'Active',
        'coment':'Perosna medio loca',
    }
    
    epp_1=[{'type':'Casco', 'serial_number':'csc1234', 'manufacturer':'MSA', 'asign_date':'12-4-2022'},{'type':'Anteojos', 'serial_number':'antdd53234', 'manufacturer':'North', 'asign_date':'30-1-2021'},
    {'type':'Zapatos', 'serial_number':'boots1234', 'manufacturer':'Honeywell', 'asign_date':'2-8-2009'}]
    

    context={"empleado":employee_1, 
             "epps":epp_1}
    return render(request,'employee/employee_details.html', context )
    


def baja_empleado(request):
    # Mark the selected employee as deleted in the DB
    Baja_Empleado= BajaEmpleadoForm()
    context={'form': Baja_Empleado}

    print(request.POST)
    return render(request,'employee/BajaEmpleados.html', context )

    
def employee_new(request):
    # Show the form to load a new employee
    if request.method == "POST":
        employee_new_form=Employee(request.POST)    
        if employee_new.is_valid():
            messages.add_message(request, messages.SUCCESS, 'El EPP fue cargado correctamente')        
            return redirect("/empleados/employee_details/" + fname)
        else:
            messages.error(request, 'Error al grabar los datos, por favor verifique los datos ingresados')
    else:
        employee_new_form=Employee()
    context= {'form_new_employee': employee_new_form}
    return render(request,'employee/employee_new.html' , context)

