from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse


def epp_list(request):
    in_stock=[{'type':'Casco001', 'serial_number':'csc1234', 'manufacturer':'MSA', 'asign_date':'12-4-2022'},{'type':'Anteojos', 'serial_number':'antdd53234', 'manufacturer':'North', 'asign_date':'30-1-2021'},
    {'type':'Zapatos', 'serial_number':'boots1234', 'manufacturer':'Honeywell', 'asign_date':'2-8-2009'}]
    assigned=[{'type':'Casco11', 'serial_number':'11csc1234', 'manufacturer':'MSA11', 'asign_date':'12-4-2011'},{'type':'Anteojos11', 'serial_number':'11antdd53234', 'manufacturer':'North', 'asign_date':'30-1-2021'},
    {'type':'Zapatos11', 'serial_number':'boots1234', 'manufacturer':'Honeywell', 'asign_date':'2-8-2009'}]
    to_expire=[{'type':'Casco22', 'serial_number':'csc1234', 'manufacturer':'MSA', 'asign_date':'12-4-2022'},{'type':'Anteojos22', 'serial_number':'antdd53234', 'manufacturer':'North', 'asign_date':'30-1-2021'},
    {'type':'Zapatos22', 'serial_number':'boots1234', 'manufacturer':'Honeywell', 'asign_date':'2-8-2009'}]
    to_inspect=[{'type':'Casco333', 'serial_number':'csc1234', 'manufacturer':'MSA', 'asign_date':'12-4-2022'},{'type':'Anteojos33', 'serial_number':'antdd53234', 'manufacturer':'North', 'asign_date':'30-1-2021'},
    {'type':'Zapatos33', 'serial_number':'boots1234', 'manufacturer':'Honeywell', 'asign_date':'2-8-2009'}]
    employees=[{'name':'Alejandro', 'surname':'Giudici'},
    {'name':'Sofia', 'surname':'Forastier'},
    {'name':'Juan Carlos', 'surname':'Galan'},
    {'name':'Marcelo', 'surname':'Gon'}]

    context={"in_stock":in_stock, "assigned":assigned,"to_expire":to_expire, "to_inspect":to_inspect,"employees":employees }
    return render(request,'epp/resume.html', context)

def epp_new(request):
    pass



