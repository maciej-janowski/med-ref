from random import choices
from django.forms import ModelForm
# from .models import
from django import forms
from time import timezone
from django.contrib.auth.models import User
from .models import Clinic,Test,TestType
from django.contrib.auth.forms import UserCreationForm

from django.core import validators

# form for creating a user
class UserRegisterForm(UserCreationForm):
    CHOICES = (
        ('Male',"Male"),
        ('Female',"Female")
    )

    email = forms.EmailField()
    name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=30)
    phone = forms.CharField(max_length=9)
    pesel = forms.CharField(max_length=11)
    date_of_birth = forms.DateField(widget=forms.DateTimeInput(attrs={
            'type':"date"
        }))
    city = forms.CharField(max_length=25)
    street = forms.CharField(max_length=50)
    street_no = forms.CharField(max_length=5)
    flat_no = forms.CharField(max_length=5)
    # establishing patter for postal code
    postal_code = forms.CharField(max_length=6,widget=forms.TextInput(attrs={'pattern':"\d{2}-\d{3}",
                                                                        'placeholder':'91-000'}))

    sex = forms.CharField(max_length=6,widget=forms.Select(choices=CHOICES))
    # selecting fields for entry by new users
    class Meta:
        model = User
        fields = ['username','password1','password2','name','last_name','email','phone','date_of_birth','city','street','street_no','flat_no','postal_code','sex']


# form for registering new medic
class MedicRegisterForm(UserCreationForm):


    name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=30)
    doc_number = forms.CharField(max_length=9)
    clinic_info = forms.ModelChoiceField(queryset=Clinic.objects.all())
    

    class Meta:
        model = User
        fields = ['username','password1','password2','name','last_name','doc_number','clinic_info']

# form for filling in the medical referal
class ReferalForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = "__all__"
