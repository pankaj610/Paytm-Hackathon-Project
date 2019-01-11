
from django.shortcuts import render,get_object_or_404
from .models import Hospital,Doctor
def doctor_list(request,hospital_slug=None):
    hospital=None
    hospitals=Hospital.objects.all()
    doctors=Doctor.objects.filter(available=True)
    if hospital_slug:
        hospital=get_object_or_404(Hospital,slug=hospital_slug)
        doctors=Doctor.objects.filter(category=hospital)
    context={
        'hospital':hospital,
        'hospitals':hospitals,
        'doctors':doctors
    }
    return render (request,'list.html',context)

def doctor_detail(request,id,slug):
    doctor=get_object_or_404(Doctor,id=id,slug=slug)
    context={
        'doctor':doctor
    }
    return render(request,'detail.html',context)


def ambulance_detail(request,id,slug):
    ambulance=get_object_or_404(Ambulance,id=id,slug=slug)
    context={
        'ambulance':ambulance
    }
    return render(request,'ambulance_detail.html',context)
