from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .cart import Cart
from store.models import Product

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
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product)
    print(request.session['session_key'])
    print(cart.cart)
    cart_quantity = cart.__len__()
    response = JsonResponse({'cart_quantity': cart_quantity, })

    return response
