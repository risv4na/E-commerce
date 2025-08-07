from django.urls import path
from .views import *

urlpatterns = [
    path('cart_summery/', cart_summery, name='cart_summery'),
    path('cart_add/', cart_add, name='cart_add'),
    path('cart_delete/', cart_delete, name='cart_delete'),
    path('cart_update/', cart_update, name='cart_update'),

] 
