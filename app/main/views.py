from django.shortcuts import render,redirect
from main.form import RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

# @login_required(login_url='login')
def index (request):

    return render(request,'base/base.html')

def error (request):
    return render(request,'base/404.html')
def table(request):

    return render(request,'base/tables.html')

def forgot_password(request):
    return render(request,'base/forgot-password.html')


def HomeSinPrivilegios(request):

    return render(request,'base/sin_privilegios.html')



def register_page(request):
    if request.user.is_authenticated:
            return redirect('index')
    else:    
            register_form =RegisterForm()
            if request.method == 'POST':
                register_form=RegisterForm(request.POST)
                if register_form.is_valid():

                    register_form.save()
                    messages.success(request,'Te has registrado correctamente')
                    return redirect('index')
            
            return render(request,'base/register.html',{
                'title': 'registro',
                'register_form': register_form,


        })
 


def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:   
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user= authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            
            else:
                messages.warning(request,'No te has podido iniciar correctamente')

        return render(request,'base/login.html', {
            'title':'Identificate',


    })

def logout_user(request):
    logout(request)
    return redirect('login')