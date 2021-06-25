from django import forms
from django.core import validators
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth.models import User 


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields=['username','first_name','last_name','email','password1','password2']
        
    
    username = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control form-control-user",'placeholder':"Username"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control form-control-user",'placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control form-control-user",'placeholder':'Last Name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control form-control-user",'placeholder':'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control form-control-user",'placeholder':'Password'}))
    password2= forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control form-control-user",'placeholder':'Repeat Password'}))

    