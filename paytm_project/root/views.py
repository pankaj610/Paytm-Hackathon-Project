from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from . import forms
# Create your views here.
def index(request):

    return render(request, 'index.html')

def register(request):
    signup_form = forms.SignUpForm()
    return render(request, 'register.html',{'form':signup_form})

def bookAmbulance(request):
    print(request.method)
    if request.method == 'POST':
        form = forms.BookAmbulanceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<html><script>thankyou</script></html>')
        else:
            print("Nooooooooooooo")
    else:
        ambulance = forms.BookAmbulanceForm()
    return render(request, 'bookambulance.html',{'form':ambulance})
