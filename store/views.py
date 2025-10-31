from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='login_view')
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products' : products})

# @login_required(login_url='login_view')
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


def product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'product.html', {'product':product})

# @login_required(login_url='login_view')
def category(request, category_name):
    category = Category.objects.get(name=category_name)
    products = Product.objects.filter(category=category)
    return render(request, 'home.html', {'products' : products})
    


def update_user(request):
    if request.user.is_authenticated: 
        current_user = User.objects.get(id=request.user.id)
        user_update_form = forms.UpdateUserFrom (request.POST or None, instance=current_user )

        if user_update_form.is_valid():
            user_update_form.save()

            login(request,current_user)
            messages.success(request,'User has been updated!!!')
            return redirect('home')
        return render(request, "update_user.html", {'user_update_form':user_update_form})
    else:
        messages.success(request, "You must be logged in to access this page..")
        return redirect('home')
 

def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == "POST":
            form = forms.ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                login(request,current_user)
                messages.success(request,'Your password has been updated successfully!!')
                return redirect('home')
            else:
                for error in list(form.errors.values()):
                    messages.error(request,error)
                form = forms.ChangePasswordForm(current_user)
                return render(request, "update_password.html", {'form':form})
        else:
            form = forms.ChangePasswordForm(current_user)
            return render(request, "update_password.html", {'form':form})
    else:
        messages.success(request, "You must be logged in to access this page..")
        return redirect('home')