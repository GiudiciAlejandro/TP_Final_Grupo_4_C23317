from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from .forms import New_epp


def epp_list(request):
    in_stock=[{'type':'Casco001', 'serial_number':'csc1234', 'manufacturer':'MSA', 'asign_date':'12-4-2022'},{'type':'Anteojos', 'serial_number':'antdd53234', 'manufacturer':'North', 'asign_date':'30-1-2021'},
    {'type':'Zapatos', 'serial_number':'boots1234', 'manufacturer':'Honeywell', 'asign_date':'2-8-2009'}]
    assigned=[{'type':'Casco11', 'serial_number':'11csc1234', 'manufacturer':'MSA11', 'asign_date':'12-4-2011'},{'type':'Anteojos11', 'serial_number':'11antdd53234', 'manufacturer':'North', 'asign_date':'30-1-2021'},
    {'type':'Zapatos11', 'serial_number':'boots1234', 'manufacturer':'Honeywell', 'asign_date':'2-8-2009'},
    {'type':'Zapatos11', 'serial_number':'boots1234', 'manufacturer':'Honeywell', 'asign_date':'2-8-2009'},
    {'type':'Zapatos11', 'serial_number':'boots1234', 'manufacturer':'Honeywell', 'asign_date':'2-8-2009'}]
    to_expire=[{'type':'Casco22', 'serial_number':'csc1234', 'manufacturer':'MSA', 'asign_date':'12-4-2022'},
    {'type':'Zapatos22', 'serial_number':'boots1234', 'manufacturer':'Honeywell', 'asign_date':'2-8-2009'}]
    to_inspect=[{'type':'Anteojos33', 'serial_number':'antdd53234', 'manufacturer':'North', 'asign_date':'30-1-2021'},
    {'type':'Zapatos33', 'serial_number':'boots1234', 'manufacturer':'Honeywell', 'asign_date':'2-8-2009'}]
    employees=[{'name':'Alejandro', 'surname':'Giudici'},
    {'name':'Sofia', 'surname':'Forastier'},
    {'name':'Juan Carlos', 'surname':'Galan'},
    {'name':'Marcelo', 'surname':'Gon'}]

    context={"in_stock":in_stock, "assigned":assigned,"to_expire":to_expire, "to_inspect":to_inspect,"employees":employees }
    return render(request,'epp/resume.html', context)

def epp_new(request):
    if request.method == "POST":
        epp_form = New_epp(request.POST)
        # Validations
        if epp_form.is_valid():
            # TODO add validate for date not before to actual date
            return redirect("/epp/epp_new")
    else:
        epp_form = New_epp()
    context = {'form_epp': epp_form}
    return render(request,'epp/alta_epp.html', context)

    

