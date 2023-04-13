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
    
    context={"empleado":employee_1}
    return render(request,'employee/employee_details.html', context )
    

def employee_new(request):
    # Show the form to load a new employee
    pass


def employee_delete(employee):
    # Mark the selected employee as deleted in the DB
    pass
