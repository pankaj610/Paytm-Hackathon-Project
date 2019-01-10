from django.shortcuts import render,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from . import models
# Create your views here.
def index(request):

    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():

            form.save()
            return HttpResponse("<html><script>alert('Thankyou For Registering');window.location = '/root/';</script></html>")
    signup_form = forms.SignUpForm()
    return render(request, 'register.html',{'form':signup_form})



def bookAmbulance(request):
    if request.method == 'POST':
        form = forms.BookAmbulanceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<html><script>alert('Your information send to nearby hospital.');window.location = '/root/';</script></html>")
    else:
        ambulance = forms.BookAmbulanceForm()
    return render(request, 'bookambulance.html',{'form':ambulance})

def login(request):
    if request.method == 'POST':
        user = get_object_or_404(models.SignUp,aadhar=str(request.POST['aadhar']), user_type=str(request.POST['user_type']), password=str(request.POST['password']))
        if user.user_type=="ambulance":
            return HttpResponseRedirect('/ambulance/')
        elif user.user_type=="hospital":
            return HttpResponseRedirect('/hospital/')
        elif user.user_type=="patient":
            return HttpResponseRedirect('/user/')

    loginform = forms.LoginForm()
    return render(request, 'login.html',{'form':loginform})
