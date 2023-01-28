from django.urls import include, path
from rest_framework.routers import DefaultRouter


from .views import *

router = DefaultRouter()
#router.register(r'order', views.ItemViewSet, basename="order")

urlpatterns = [
    path('create/', CreateOrder.as_view(), name='CreateOrder'),
    path('get_status/', GetOrderStatus.as_view(), name='CreateItemOrder')
]
