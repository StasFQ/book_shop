import django_filters
from django_filters import CharFilter
from .models import Book


class BookFilter(django_filters.FilterSet):
    title = CharFilter(field_name="title", lookup_expr="icontains")
    price = django_filters.NumberFilter()

    class Meta:
        model = Book
        fields = '__all__'
