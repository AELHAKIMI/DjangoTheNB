from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import patient, dossierPatient, service
from django.template import loader

# Create your views here.

def index(request):
    return render(request, 'index.html' )


def Dossierindex(request):
    all_dossier = dossierPatient.objects.all()    
    context = {'all_dossier' : all_dossier}
    return render(request , 'dossierPatient/index.html', context)


def Patientindex(request):
    all_patients = patient.objects.all()    
    context = {'all_patients' : all_patients}
    return render(request , 'Patient/index.html', context)


def ServiceIndex(request):
    all_Services = service.objects.all()
    context = {'all_Services': all_Services}
    return render(request, 'Service/index.html', context)


def detailPatient(request, patient_id):
    try:
        PatientRow = patient.objects.get(patientID = patient_id)
        titles = ('N', 'Patient ID', 'Patient Name')
        Patient = (PatientRow.id, PatientRow.patientID, PatientRow.patientName) 
        context ={
            'the_row_title' : titles,
            'Patient'        : Patient
        }  
             
    except patient.DoesNotExist:
        raise Http404('Patient does Not Exist')    
    return render(request , 'Patient/detail.html', context ) 

def detailDossierPatient(request, dossierpatient_id):
    try:
        dossierpatient = dossierPatient.objects.get(id = dossierpatient_id)
        titles = ('Number', 'Dossier ID', 'Patient', 'Service')
        dossier = (dossierpatient.id, dossierpatient.DossierID, dossierpatient.patientID  , dossierpatient.serviceID)
        context = {
            'the_row_title' : titles,
            'dossier'   : dossier
        } 
               
    except dossierPatient.DoesNotExist:
        raise Http404('dossier does Not Exist')    
    return render(request , 'dossierPatient/detail.html', context )

def detailService(request, service_id):
    try:
        ServiceRow = service.objects.get(id = service_id)
        titles = ('N', 'Service ID', 'Service')
        Service = (ServiceRow.id, ServiceRow.serviceID, ServiceRow.service)
        context ={
            'the_row_title' : titles,
            'Service'       : Service
        }
    except service.DoesNotExist:
        raise Http404('Service Does Not Exist')
    return render(request , 'Service/detail.html', context)

    