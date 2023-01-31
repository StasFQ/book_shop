from rest_framework import serializers

from .models import Order, OrderItem, Book, BookItem, OrderItemBookItem


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ['order', 'book', 'quantity']
        read_only_fields = ['order', ]


class OrderSerializer(serializers.ModelSerializer):
    order_item = OrderItemSerializer(many=True, write_only=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        order = Order.objects.create(user_email=validated_data['user_email'],
                                     status=validated_data['status'],
                                     delivery_adress=validated_data['delivery_adress'],
                                     order_id_in_shop=validated_data['order_id_in_shop'])
        batch = [OrderItem(book=item['book'], order=order, quantity=item['quantity']) for item in validated_data['order_item']]
        order.orderitem_set.bulk_create(batch)
        return order


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class BookItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookItem
        fields = '__all__'
        read_only_fields = ['order', ]


class BookSerializer(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(many=True, read_only=True, source='bookitem_set')

    class Meta:
        model = Book
        fields = ['id', 'title', 'price', 'book']


class OrderItemBookItemSerializer(serializers.ModelSerializer):
    order_item = serializers.HyperlinkedRelatedField(many=True, view_name='orderitem-detail',
                                                     read_only=True)
    book_item = serializers.HyperlinkedRelatedField(many=True, view_name='bookitem-detail',
                                                    read_only=True)

    class Meta:
        model = OrderItemBookItem
        fields = ['id', 'order_item', 'book_item']