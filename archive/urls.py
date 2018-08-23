from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    #/archive/
    url(r'^$', views.index , name='index'),

    #/archive/229/
    url(r'^(?P<patient_id>[0-9]+)/$', views.detailPatient, name='detailpatient')

]


    
