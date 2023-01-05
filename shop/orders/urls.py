from django.template.defaulttags import url
from django.urls import path

from . import views
from .views import *
from .views import RegisterFormPage

appname = 'orders'
urlpatterns = [
    path('register/', RegisterFormPage.as_view(), name='RegisterFormPage'),
    path('book_list/', search_books, name='search_books'),
    path('cart_detail/', views.cart_detail, name='cart_detail'),
    path('add/<int:pk>', views.cart_add, name='cart_add'),
]
