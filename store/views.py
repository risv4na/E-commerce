from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .import forms
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
import json
from cart.cart import Cart

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
            current_user = CustomerProfile.objects.get(user__id=request.user.id)
            current_user.save()

            old_cart = current_user.old_cart
            #converet db string into dictionary 
            if old_cart:
                converted_cart = json.loads(old_cart)
                cart = Cart(request)

                for key,value in converted_cart.items():
                    cart.add(product=key, quantity=value, db=True)


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
            user = form.save()
            profile = CustomerProfile.objects.create(user=user)
            profile.save()
            update_form = forms.UserInfoForm(request.POST or None, instance=current_user )
            return render(request, "update_user_info.html", {'update_form':update_form})
            # return redirect('update_user_info')
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


def update_user_info(request):
    if request.user.is_authenticated: 
        current_user = CustomerProfile.objects.get(user__id=request.user.id)
        update_form = forms.UserInfoForm(request.POST or None, instance=current_user )

        if update_form.is_valid():
            update_form.save()
            messages.success(request,'User Profile has been updated!!!')
            return redirect('login_view')
        return render(request, "update_user_info.html", {'update_form':update_form})
    else:
        messages.success(request, "You must be logged in to access this page..")
        return redirect('home')


# def search_product(request):
#     if request.method == "POST":
#         item = request.POST.get('searched')
#         products = Product.objects.filter(Q(name__icontains=item) or Q())
#         if products:
#             return render(request, 'home.html', {'products' : products})
#         else:
#             messages.success(request,"No products found!!!")
#             return redirect('home')

def search_product(request):
    if 'term' in request.GET:
        print("got it",'term')
        products = Product.objects.filter(Q(name__istartswith=request.GET.get('term')) | Q(description__icontains=request.GET.get('term'))) 
        name = list()
        
        for product_name in products:
            name.append(product_name.name)
        return JsonResponse(name ,safe=False)
    if request.method == 'POST':
        search = request.POST.get('searched')
        products = Product.objects.filter(
            Q(name__icontains=search) | 
            Q(description__icontains=search)
        )

    
        return render(request, 'home.html', {'products' : products})

