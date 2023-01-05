from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST

from .cart import Cart
from .filters import BookFilter
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import RegisterForm, CartAddProductForm, Checkout
from .models import Book


class RegisterFormPage(generic.FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('/')

    def form_valid(self, form):
        user = form.save()
        user = authenticate(username=user.username, password=form.cleaned_data.get('password1'))
        login(self.request, user)
        return super(RegisterFormPage, self).form_valid(form)


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


def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    cart_product_form = CartAddProductForm()
    return render(request, "shop/book_detail.html", {"book": book, 'cart_product_form': cart_product_form})


def checkout(request):
    form = Checkout()
    return render(request, 'shop/checkout.html', {'form': form})
