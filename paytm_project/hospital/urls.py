from django.shortcuts import render
from django.conf.urls import url
from . import views
app_name = 'hospital'
urlpatterns = [
    url(r'', views.doctor_list, name = 'doctor_list'),
    url(r'^(?P<doctor_slug>[-\w]+)/$', views.doctor_list, name = 'doctor_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.doctor_detail, name = 'doctor_detail'),
    url(r'^ambulance/(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.ambulance_detail, name = 'ambulance_detail'),

]
