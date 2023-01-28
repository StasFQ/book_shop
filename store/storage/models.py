
from django.db import models



class Book(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(decimal_places=2, max_digits=4)


class BookItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    place = models.CharField(max_length=254)


class Order(models.Model):
    user_email = models.EmailField()
    status = models.BooleanField()
    delivery_adress = models.CharField(max_length=254)
    order_id_in_shop = models.IntegerField()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class OrderItemBookItem(models.Model):
    order_item = models.ForeignKey(OrderItem, on_delete=models.CASCADE)
    book_item = models.ForeignKey(BookItem, on_delete=models.CASCADE)
