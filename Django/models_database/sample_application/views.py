from django.shortcuts import render
from django.http.response import HttpResponse
from . import models

def list_patients(req):
    all_patients = models.Patient.objects.all();
    
    return render(req,'sample_application/list.html',context={"data":all_patients})
