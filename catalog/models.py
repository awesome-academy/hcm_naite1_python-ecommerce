from itertools import product
from django.db import models
from django.urls import reverse  
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
<<<<<<< HEAD
import catalog.constants as c 
=======
import catalog.constants as c   
>>>>>>> Show Cake

class Customer (models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
<<<<<<< HEAD
        return str(self.name)   
=======
        return str(self.name)
    
>>>>>>> Show Cake
class Address(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=c.ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.street_address

    class Meta:
        verbose_name_plural = 'Addresses'

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    quantity = models.IntegerField(default=0)
        
    def __str__(self):
        return self.title
    @property
    def imageURL(self):
        try: 
            url = self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True,null=True)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    ordered_date = models.DateTimeField()
    status = models.CharField(
        max_length = c.LENGTH,
        choices = c.STATUS_CHOICE,
        blank = True,
        default = 'N',
        help_text = _('Status Order'),
    )
    shipping_address = models.ForeignKey(
        'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey(
        'Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey(
        'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.customer.name
    
class OrderProduct(models.Model):
        
<<<<<<< HEAD
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=c.LENGTH)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,blank=True, null=True)

    def __str__(self):
        return f"{self.quantity} of {self.product.title}"

=======
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,blank=True, null=True)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

>>>>>>> Show Cake
    
class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()
    
    def __str__(self):
        return self.code
