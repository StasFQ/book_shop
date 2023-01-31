from django.core.mail import send_mail as django_send_mail
import requests
from celery import shared_task

from .models import Order, Book


@shared_task()
def send_email(subject, text, email_sender):
    django_send_mail(subject, text, email_sender, ['admin@example.com'])


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
    order = Order.objects.filter(status=False)
    order_ids = order.values_list('id', flat=True)

    r = requests.get('http://storage:8001/api/get_status/', params={'order_id_in_shop': list(order_ids)})
    if r.status_code == 200:
        orders_from_store = r.json()
        for store_order in orders_from_store:
            order = Order.objects.get(id=store_order['order_id_in_shop'])
            order.status = store_order['status']
            order.save()
    else:
        sync_orders.apply_async(countdown=15)

@shared_task()
def sync_book():
    r = requests.get('http://storage:8001/api/book/')
    if r.status_code == 200:
        responce = r.json()
        for r in responce:
            Book.objects.update_or_create(
                         title=r['title'],
                         price=r['price'],
                         id_in_store=r['id'],
                         quantity=len(r['book']))
    else:
        sync_book.apply_async(countdown=20)
