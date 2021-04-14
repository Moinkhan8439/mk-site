from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserRegisterForm,UserLoginForm
from django.contrib.auth import authenticate, login , logout
from internal.views import home
from django import forms

# Create your views here.
def register(request):
    form=UserRegisterForm()
    if request.method == 'POST':
        form=UserRegisterForm(data=request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect(user_login)
        else:
            return render(request,'register-form.html',{'form': form})
    else:
        return render(request,'register-form.html',{'form': form})


def user_login(request):
    form=UserLoginForm()
    if request.method == 'POST':
        form=UserLoginForm(request.POST)
        if form.is_valid():
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect('internal:home')
        print(dir(form))
        print(form.non_field_errors)
        return render(request,'login-form.html',{'form': form })   
    else:    
        return render(request,'login-form.html',{'form': form })

def user_logout(request):
    logout(request)
    return redirect('internal:home')