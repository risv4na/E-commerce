from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def payment_success(request):
    return render(request, "payment_success.html")