
from django.shortcuts import get_object_or_404
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_POST

from . import tasks
from .cart import Cart
from .filters import BookFilter
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import CartAddProductForm, Checkout, OrderCreateForm
from .models import Book, OrderItem


@require_POST
def cart_add(request, book_id):
    cart = Cart(request)
    product = get_object_or_404(Book, id=book_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])

    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'shop/detail.html', {'cart': cart})


def search_books(request):
    books = Book.objects.all()
    myFilter = BookFilter(request.GET, queryset=books)
    books = myFilter.qs

    context = {"books": books, "myFilter": myFilter}
    return render(request, "shop/search_book.html", context)


@cache_page(15)
def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    cart_product_form = CartAddProductForm()
    return render(request, "shop/book_detail.html", {"book": book, 'cart_product_form': cart_product_form})


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.status = False
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         book=item['product'],
                                         quantity=item['quantity'])
            subject = 'Order create'
            text = 'I create order'
            email_sender = request.user.email
            tasks.send_email.delay(subject, text, email_sender)
            cart.clear()
            tasks.send_order_to_store.delay(order.id)
            return render(request, 'shop/order_created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'shop/orders.html',
                  {'cart': cart, 'form': form})


def checkout(request):
    form = Checkout()
    return render(request, 'shop/checkout.html', {'form': form})
