from .cart import Cart

def cart_data(request):
    return {'cart':Cart(request)}