from django.urls import path
from .views import *


urlpatterns = [
    path('create/', CreateOrder.as_view(), name='CreateOrder'),
    path('get_status/', GetOrderStatus.as_view(), name='CreateItemOrder')
]
