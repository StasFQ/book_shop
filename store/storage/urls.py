from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import *
router = DefaultRouter()
router.register(r'orderitembookitem', views.BookItem, basename='orderitembookitem')
router.register(r'book', views.BookViewSet, basename="book")
urlpatterns = [
    path('create/', CreateOrder.as_view(), name='CreateOrder'),
    path('get_status/', GetOrderStatus.as_view(), name='CreateItemOrder'),
    path('', include(router.urls)),
]
