from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import RegisterForm


class RegisterFormPage(generic.FormView):
    template_name = 'registration/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('orders:search_books')

    def form_valid(self, form):
        user = form.save()
        user = authenticate(username=user.username, password=form.cleaned_data.get('password1'))
        login(self.request, user)
        return super(RegisterFormPage, self).form_valid(form)


@login_required
def profile(request):
    user = request.user
    return render(request, 'user/profile.html', {'user': user})
