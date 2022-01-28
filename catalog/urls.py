from django.urls import path,include,re_path
from . import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
]
