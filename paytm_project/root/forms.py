from django import forms
from . import models
from easy_maps.widgets import AddressWithMapWidget

# from bootstrap_datepicker_plus import DatePickerInput
GENDER_CHOICES=(('male','MALE'),('female','FEMALE'))
USER_CHOICES=(('ambulance','AMBULANCE'),('hospital','HOSPITAL'),('patient','PATIENT'))
class SignUpForm(forms.ModelForm):
    # name = forms.CharField(widget=, required=True ,max_length = 20)
    # emailid = forms.CharField(, required=True ,max_length = 30)
    # aadhar = forms.CharField(widget=, required=True , max_length=12)
    gender = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=GENDER_CHOICES,required=True)
    user_type = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=USER_CHOICES,required=True)
    dob = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control mb-2 mr-sm-2','type': 'date'}),required=True)
    class Meta:
        model= models.SignUp
        fields=['name','username','email','gender','aadhar','dob','user_type','password']
        widget={
            'name':forms.TextInput(attrs={'class':'form-control mb-2 mr-sm-2','placeholder':'Enter Full Name'}),
            'username':forms.TextInput(attrs={'class':'form-control mb-2 mr-sm-2','placeholder':'Enter Username'}),
            'email':forms.TextInput(attrs={'class':'form-control mb-2 mr-sm-2','placeholder':'Enter Valid Email'}),
            # 'gender':,
            'aadhar':forms.NumberInput(attrs={'class':'form-control mb-2 mr-sm-2','placeholder':'Enter Your 16 digit Aadhar Number'}),
            'password':forms.PasswordInput(attrs={'class':'form-control mb-2 mr-sm-2','placeholder':'Enter Password'})
        }

class BookAmbulanceForm(forms.ModelForm):
    # name = forms.CharField(widget=, required=True ,max_length = 20)
    # emailid = forms.CharField(, required=True ,max_length = 30)
    # aadhar = forms.CharField(widget=, required=True , max_length=12)
    # gender = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=GENDER_CHOICES,required=True)
    # user_type = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=USER_CHOICES,required=True)
    # dob = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control mb-2 mr-sm-2','type': 'date'}),required=True)
    class Meta:
        model= models.BookAmbulance
        fields=['accident_location_picture','long','lat']


class LoginForm(forms.Form):
    user_type = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=USER_CHOICES,required=True)
    aadhar = forms.IntegerField(widget = forms.NumberInput(attrs={'class':'form-control mb-2 mr-sm-2','placeholder':'Enter Your 16 digit Aadhar Number'}), required=True)
    password = forms.CharField(widget = forms.PasswordInput(attrs={'class':'form-control mb-2 mr-sm-2','placeholder':'Enter Password'}),required=True)
