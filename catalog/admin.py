from django.contrib import admin
from .models import *
    
admin.site.register(Address)
admin.site.register(Product)
admin.site.register(OrderProduct)
admin.site.register(Order)
admin.site.register(Coupon)
admin.site.register(Customer)
