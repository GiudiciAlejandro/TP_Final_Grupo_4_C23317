from django.urls import path, re_path
from . import views

urlpatterns = [
    path('epp_list/', views.epp_list, name='epp_list'), # Show epp list
    path('epp_new/', views.epp_new, name='epp_new'), # Add an epp to the DB
    path('epp_type/', views.epp_type, name='epp_type'), # Add an epp type to the DB
    path('epp_detail/<int:id>', views.epp_detail, name='epp_detail'),
    path('epp_update/<int:id>', views.epp_update, name='epp_update'),
    path('insp_new/', views.insp_new, name='insp_new'),

]