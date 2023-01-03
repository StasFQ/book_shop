from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=254)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField()
    id_in_store = models.IntegerField()

