import django_filters
from django.shortcuts import render
from rest_framework import viewsets, generics
from django_filters import rest_framework as filters
from .models import Order, OrderItem, Book, OrderItemBookItem
from .serializer import OrderSerializer, OrderItemSerializer, OrderStatusSerializer, BookSerializer, \
    OrderItemBookItemSerializer


class OrderFilter(django_filters.FilterSet):

    class Meta:
        model = Order
        fields = {
            'order_id_in_shop': ['in']
        }


class CreateOrder(generics.CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class GetOrderStatus(generics.ListAPIView):
    serializer_class = OrderStatusSerializer
    queryset = Order.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = OrderFilter


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookItem(viewsets.ModelViewSet):
    queryset = OrderItemBookItem.objects.all()
    serializer_class = OrderItemBookItemSerializer
