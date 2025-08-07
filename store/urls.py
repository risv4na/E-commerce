from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('user_register/', user_register, name='user_register'),
    path('product/<int:id>/', product, name='product'),
]
