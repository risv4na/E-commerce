from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('user_register/', user_register, name='user_register'),
    path('product/<int:id>/', product, name='product'),
    path('category/<str:category_name>/', category, name='category'),
    path('update_user/', update_user, name='update_user'),
]
