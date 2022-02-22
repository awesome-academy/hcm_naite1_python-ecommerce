from itertools import product
from venv import create
from django.shortcuts import render
from django.template import context
from django.utils.translation import gettext as _
from .models import *
from django.shortcuts import get_object_or_404

def store(request):
    products = Product.objects.order_by('price')
    context = {'products':products}
    return render(request, 'store/store.html', context)

def cart(request):
    products = Product.objects.order_by('price')
    context = {'products':products}
    return render(request, 'store/store.html', context)

def cart (request):
    if request.user.is_authenticated:
        customer = get_object_or_404(Customer, pk=request.user.customer.id)
        order,created = Order.objects.get_or_create(customer=customer)
        items = order.orderproduct_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_products':0}
    context = {'items':items, 'order':order}
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = get_object_or_404(Customer, pk=request.user.customer.id)
        order,created = Order.objects.get_or_create(customer=customer)
        items = order.orderproduct_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_products':0}
    context = {'items':items, 'order':order}
    return render(request, 'store/checkout.html', context)
