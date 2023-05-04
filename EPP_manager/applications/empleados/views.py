from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
# Create your views here.


def employee_lits(request):
    # Show a list of all employees names and surname
    # Clicking in one employee open employee_details page
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
        'mobile_n':'+5491123456789',
        'status': 'Active'
    }
    
    epp_1=[{'type':'Casco', 'serial_number':'csc1234', 'manufacturer':'MSA', 'asign_date':'12-4-2022'},{'type':'Anteojos', 'serial_number':'antdd53234', 'manufacturer':'North', 'asign_date':'30-1-2021'},
    {'type':'Zapatos', 'serial_number':'boots1234', 'manufacturer':'Honeywell', 'asign_date':'2-8-2009'}]
    

    context={"empleado":employee_1, 
             "epps":epp_1}
    return render(request,'employee/employee_details.html', context )
    

def employee_new(request):
    # Show the form to load a new employee
    pass


def employee_delete(employee):
    # Mark the selected employee as deleted in the DB
    pass

def alta_empleado(request):
    
    context={}

    print(request.POST)
    return render(request,'employee/altanuevoempleado.html', context )