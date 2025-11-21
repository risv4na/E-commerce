
from django.urls import path
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('payment_success/', payment_success, name="payment_success"),
    path('checkout/', checkout, name="checkout"),
    path('billing_info', billing_info, name="billing_info"),
    path('process_order/', process_order, name="process_order"),
    # path('billing_info/<int:id>', billing_info, name="billing_info"),

] 
