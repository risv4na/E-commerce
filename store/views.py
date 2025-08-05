from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .import forms

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products' : products})


def about(request):
    return render(request, 'about.html', {})


def login_view(request):
    if request.method == 'POST':
        print("heyyyy reached here....")
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user:
            login(request,user)
            messages.success(request, 'You have been login succesfully.')
            return redirect('home')
        else:
            return render(request, 'login_view.html', {'error':'Incorrect password or username.Try again!!'})
    return render(request, 'login_view.html', {})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return render(request, 'login_view.html', {})

def user_register(request):
    form = forms.SignUpForm()
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'login_view.html', {})
    return render(request, 'user_register.html', {'form':form})