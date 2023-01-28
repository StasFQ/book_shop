from rest_framework import serializers

from .models import Order, OrderItem


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
