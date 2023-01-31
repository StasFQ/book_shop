from django.shortcuts import render
from rest_framework import viewsets, generics

from .models import Order, OrderItem, Book, OrderItemBookItem
from .serializer import OrderSerializer, OrderItemSerializer, OrderStatusSerializer, BookSerializer, \
    OrderItemBookItemSerializer


class CreateOrder(generics.CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class GetOrderStatus(generics.ListAPIView):
    serializer_class = OrderStatusSerializer
    queryset = Order.objects.all()


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookItem(viewsets.ModelViewSet):
    queryset = OrderItemBookItem.objects.all()
    serializer_class = OrderItemBookItemSerializer
