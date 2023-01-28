from django_filters import rest_framework as filters

from .models import Order


class ProductFilter(filters.FilterSet):
    pass
    # class Meta:
    #     model = Order
    #     fields = {'order_id_in_shop': '__in'}
