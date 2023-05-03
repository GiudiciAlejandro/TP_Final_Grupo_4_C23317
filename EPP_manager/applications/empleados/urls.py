from django.urls import path, re_path
from . import views

urlpatterns = [
    path('employee_list/', views.employee_lits, name='employee_list'), # Show employees list
    path('employee_details/<str:employee>/', views.employee_details, name='employee_details'), # show employee details with assigned EPPs
    path('employee_new/', views.employee_new, name='employee_new'),   # Add an employee to the DB
    path('bajaEmpleado/', views.baja_empleado, name='baja') 

]

