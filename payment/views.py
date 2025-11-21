from django.shortcuts import render,redirect
from django.http import HttpResponse
from cart.cart import Cart
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.

def payment_success(request):
    return render(request, "payment_success.html")

def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_products()
    quantity = cart.get_quantity()
    total = cart.cart_total()
    if request.user.is_authenticated:
        shipping_address = ShippingAddress.objects.filter(user=request.user)
    else:
        shipping_address = ShippingForm(request.POST or None)
    return render(request, 'checkout.html',{'cart_products':cart_products, 'quantity':quantity, 'total':total, 'shipping_address':shipping_address})

def billing_info(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_products()
        quantity = cart.get_quantity()
        total = cart.cart_total()
        billing_form = PaymentForm()
        if request.user.is_authenticated:
            address_id = request.POST.get("selected_address_id")
            if not address_id:
                return HttpResponse("No address selected")
            shipping_info = ShippingAddress.objects.get(id=address_id)
            return render(request, "billing_info.html", {'cart_products':cart_products, 'quantity':quantity, 'total':total, 'shipping_info':shipping_info,'billing_form':billing_form, })

        else:
            return render(request, "billing_info.html", {'cart_products':cart_products, 'quantity':quantity, 'total':total, 'shipping_info':request.POST,'billing_form':billing_form, })
    else:
        messages.success(request, "Access denied")
        return redirect('home')
        

def process_order(request):
    return render(request, "process_order.html")    


# def billing_info(request,id):
#     cart = Cart(request)
#     cart_products = cart.get_products()
#     quantity = cart.get_quantity()
    
#     print(id,"id is this.")
#     shipping_address = ShippingAddress.objects.get(id=id)
#     total = cart.cart_total()
#     return render(request, "billing_info.html", {'cart_products':cart_products, 'quantity':quantity, 'total':total})
