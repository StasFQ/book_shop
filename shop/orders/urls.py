from django.template.defaulttags import url
from django.urls import path

from . import views
from .views import *

appname = 'orders'
urlpatterns = [
    path('book_list/', search_books, name='search_books'),
    path('cart_detail/', views.cart_detail, name='cart_detail'),
    path('add/<int:book_id>', views.cart_add, name='cart_add'),
    path('book_detail/<int:id>', book_detail, name='book_detail'),
    path('order_create/', order_create, name='order_create'),
    path('checkout/', checkout, name='checkout'),
]
