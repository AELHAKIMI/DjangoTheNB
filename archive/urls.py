from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    #/archive/
    url(r'^$', views.index , name='index'),

    #/archive/Patient/
    url(r'^Patient/$', views.Patientindex, name='Patientindex'),

    #/archive/Pateint/229/
    url(r'^Patient/(?P<patient_id>[0-9]+)/$', views.detailPatient, name='detailpatient'),

    #/archive/dossierpatient/
    url(r'^dossierPatient/$', views.Dossierindex, name='dossierindex'),

    #/archive/dossierpatient/223/
    url(r'^dossierPatient/(?P<dossierpatient_id>[0-9]+)/$', views.detailDossierPatient, name='detaildossier'),

    #/archive/Service/
    url(r'^Service/$',views.ServiceIndex, name='Serviceindex' ),

    #/archive/Service/334/
    url(r'^Service/(?P<service_id>[0-9]+)/$', views.detailService, name='detailService')

]


    
