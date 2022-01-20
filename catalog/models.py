from django.db import models
from django.urls import reverse  
from django.conf import settings
from django.contrib.auth.models import User
import catalog.constants as c
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    phone = models.IntegerField()
    email = models.EmailField()
    create = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.user.username

class Address(models.Model):
    ADDRESS_CHOICES = (
        ('B', 'Billing'),
        ('S', 'Shipping'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name_plural = 'Addresses'

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField()
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
class OrderProduct(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(
            max_length=1,
            choices=c.STATUS_CHOICE,
            blank=True,
            default='N',
            help_text='Status Order',
        )    
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ref_code = models.CharField(max_length=20, blank=True, null=True)
    items = models.ManyToManyField(OrderProduct)
    ordered_date = models.DateTimeField()
    status = models.CharField(
        max_length=1,
        choices=c.STATUS_CHOICE,
        blank=True,
        default='N',
        help_text='Status Order',
    )
    shipping_address = models.ForeignKey(
        'Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    billing_address = models.ForeignKey(
        'Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey(
        'Coupon', on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.user

class Coupon(models.Model):
    code = models.CharField(max_length=15)
    amount = models.FloatField()
    
    def __str__(self):
        return self.code
