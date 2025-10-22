from django.urls import path
from .views import *

urlpatterns = [
    path('cart_summery/', cart_summery, name='cart_summery'),
    path('cart_add/', cart_add, name='cart_add'),
    path('remove_cart/', remove_cart, name='remove_cart'),
    path('cart_update/', cart_update, name='cart_update'),

] 
