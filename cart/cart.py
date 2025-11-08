from store.models import Product, CustomerProfile

class Cart:
    def __init__(self, request):

        self.request = request
        self.session = request.session
        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
        
        self.cart = cart
    
    def add(self, product, quantity, db = False):
        if db:
            product_id = str(product)
        else:
            product_id = str(product.id)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = int(quantity)

        self.session.modified = True
        print(self.cart)

        if self.request.user.is_authenticated:
            current_user = CustomerProfile.objects.get(user__id = self.request.user.id)
            old_cart = str(self.cart)
            old_cart = old_cart.replace("\'","\"")
            current_user.old_cart = old_cart
            current_user.save()

    def __len__(self):
        return len(self.cart)
    
    def get_products(self):
        products_ids = self.cart.keys()
        products = Product.objects.filter(id__in = products_ids)

        return products
    
    def remove(self, product):
        print('hey here at cart, remove')
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = CustomerProfile.objects.get(user__id = self.request.user.id)
            old_cart = str(self.cart)
            old_cart = old_cart.replace("\'","\"")
            current_user.old_cart = old_cart
            current_user.save()

        
    
    def get_quantity(self):
        return self.cart
    
    def update(self, product, product_quantity):
        product_id = str(product)
        product_quantity = product_quantity

        newcart = self.cart

        newcart[product_id] = product_quantity
        self.session.modified = True

        if self.request.user.is_authenticated:
            current_user = CustomerProfile.objects.get(user__id = self.request.user.id)
            old_cart = str(self.cart)
            old_cart = old_cart.replace("\'","\"")
            current_user.old_cart = old_cart
            current_user.save()

        return self.cart
    
    def cart_total(self):
        product_ids = self.cart.keys()
        products = Product.objects.all()
        cart = self.cart

        total = 0
        for key in products:

            if str(key.id) in list(product_ids):
                qty = int(cart[str(key.id)])
                if key.in_sale:
                    price = key.sale_price
                    total = total + (qty*price)
                else:
                    price = key.price
                    total = total + (qty*price)
        return total
    
