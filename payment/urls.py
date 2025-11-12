
from django.urls import path
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('payment_success/', payment_success, name="payment_success"),
] 
