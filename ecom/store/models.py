from django.db import models
import datetime


class Category(models.Model):
    name = models.CharField(max_length=50)


def __str__(self):
    return self.name


class Customer(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=100)
    email = models. EmailField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.First_name} {self.Last_name}'


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(
        max_length=100, default='', blank=True, null=True)
    image = models.ImageField(upload_to='upload/products/')

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    phone = models.CharField(max_length=100, default='', blank=True)

    def __str__(self):
        return self.Product
