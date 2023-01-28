from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db import models
from django_lifecycle import LifecycleModelMixin, hook, LifecycleModel, AFTER_UPDATE


class Book(models.Model):
    title = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField()
    id_in_store = models.IntegerField()

    def __str__(self):
        return self.title


class Order(LifecycleModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField()
    adress = models.CharField(max_length=254)

    @hook(AFTER_UPDATE, when="status", was=0, is_now=1)
    def on_status(self):
        send_mail('Order in a bookstore', 'You order have a new status: Success, wait for the delivery'
                                          f' of the purchase', 'bookstore@gmail.com',
                  [self.user.email],
                  fail_silently=False)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()
