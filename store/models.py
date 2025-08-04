from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Catagories"

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=9)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=1000, null=True, blank=True, default="")
    image = models.ImageField(upload_to='uploads/products')

    in_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=9)

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200, default='', blank=True, null=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
