from django.shortcuts import render
from django.http import HttpResponse


def cart_summery(request):
    print('cart summ')
    return render(request, 'cart_summery.html')

def cart_delete(request):
    print('cart delete')
    pass

def cart_update(request):
    print('cart update')
    return render(request, 'cart_update.html')

def cart_add(request):
    pass