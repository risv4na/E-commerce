from django.shortcuts import render
from .models import *
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products' : products})


def about(request):
    return render(request, 'about.html', {})


def login_view(request):
    return render(request, 'login_view.html', {})

def logout_view(request):
    return render(request, 'login_view.html', {})
