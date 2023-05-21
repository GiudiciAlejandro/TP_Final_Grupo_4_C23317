from django.urls import path, re_path
from . import views

urlpatterns = [
    path('epp_list/', views.epp_list, name='epp_list'), # Show epp list
    path('epp_new/', views.epp_new, name='epp_new'), # Add an epp to the DB
    path('epp_type/', views.epp_type, name='epp_type'), # Add an epp type to the DB

]