from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, JsonResponse
from .cart import Cart
from store.models import Product

def cart_summery(request):
    cart = Cart(request)
    cart_products = cart.get_products()
    quantity = cart.get_quantity()
    return render(request, 'cart_summery.html',{'cart_products':cart_products, 'quantity':quantity})

def remove_cart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
    print(request.session['session_key'])
    print(cart.cart)
    cart_quantity = cart.__len__()
    response = JsonResponse({'cart_quantity': cart_quantity, })
    return response

def cart_update(request):
    print('cart update')
    return render(request, 'cart_update.html')

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = request.POST.get('product_quantity')
        print(product_quantity)
        product = get_object_or_404(Product, id=product_id)
        cart.add(product, product_quantity)
    print(request.session['session_key'])
    print(cart.cart)
    cart_quantity = cart.__len__()
    response = JsonResponse({'cart_quantity': cart_quantity, })

    return response
