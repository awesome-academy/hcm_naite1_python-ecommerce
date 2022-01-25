from django.contrib import admin
from .models import UserProfile, Address, Product, OrderProduct, Order, Coupon
    
admin.site.register(UserProfile)
admin.site.register(Address)
admin.site.register(Product)
admin.site.register(OrderProduct)
admin.site.register(Order)
admin.site.register(Coupon)
