from django.shortcuts import render
from django.template import context

def catalog(request):
    context={}
    return render(request, 'catalog/catalog.html')

def cart(request):
    context={}
    return render(request, 'catalog/cart.html')

def checkout(request):
    context={}
    return render(request, 'catalog/checkout.html')