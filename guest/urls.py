from django.contrib import admin
from django.urls import path, re_path, include
from . import views as guest_view

app_name = 'guest'
urlpatterns = [
    path('', guest_view.start, name='start'),
    path('register/', guest_view.register, name='register'),
    path('login/', guest_view.user_login, name='login'),
    path('login/home/', guest_view.home, name='home'),
    path('login/select/<int:res_id>/', guest_view.select, name='select'),
    # re_path(r'profile/^$', guest_view.profile, name='profile'),
    path('login/edit/<int:res_id>/', guest_view.edit, name='edit'),
    path('login/confirm/<int:res_id>/', guest_view.confirm, name='confirm'),
    path('login/cancel/<int:res_id>/', guest_view.cancel, name='cancel'),
    path('login/pdf/<int:res_id>/', guest_view.generate_pdf, name='pdf'),
    path('login/bookings/', guest_view.bookings, name='bookings'),
    path('logout/', guest_view.logout_view, name='logout'),
]