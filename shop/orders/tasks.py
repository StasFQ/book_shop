
import requests
from celery import shared_task


from .models import Order


@shared_task()
def send_order_to_store(order_id: int):
    order = Order.objects.get(id=order_id)
    order_items = order.orderitem_set.all()

    body = {
        "order_item": [
            {
                "quantity": item.quantity,
                "book": item.book.id_in_store,
            }for item in order_items
        ],
        "user_email": order.user.email,
        "status": order.status,
        "delivery_adress": order.adress,
        "order_id_in_shop": order.id,
    }

    requests.post('http://storage:8001/api/create/', json=body)


@shared_task()
def sync_orders():
    r = requests.get('http://storage:8001/api/get_status/')
    orders_from_store = r.json()
    for store_order in orders_from_store:
        order = Order.objects.get(id=store_order['order_id_in_shop'])
        order.status = store_order['status']
        order.save()
