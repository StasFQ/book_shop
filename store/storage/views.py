from django.shortcuts import render
from rest_framework import viewsets, generics

from .models import Order, OrderItem
from .serializer import OrderSerializer, OrderItemSerializer, OrderStatusSerializer


class CreateOrder(generics.CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class GetOrderStatus(generics.ListAPIView):
    serializer_class = OrderStatusSerializer
    queryset = Order.objects.all()
