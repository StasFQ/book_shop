from django.urls import path, include

from .views import RegisterFormPage, profile

appname = 'user'
urlpatterns = [
    path('', RegisterFormPage.as_view(), name='RegisterFormPage'),
    path('profile/', profile, name='profile'),
    path('', include('django.contrib.auth.urls')),
]
