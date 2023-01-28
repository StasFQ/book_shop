from django.contrib import admin
from .models import *


admin.site.register(Book)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(OrderItemBookItem)
admin.site.register(BookItem)
