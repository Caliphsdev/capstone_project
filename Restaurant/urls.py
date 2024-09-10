from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('home', views.index, name='home'),
    path('menu', views.MenuItemView.as_view(), name= 'menu'),
    path('menu/<int:pk>', views.SingleMenuItem.as_view(), name='single_menu'),
    path('booking/create', views.BookingView.as_view(), name='booking'),
    path('api-token-auth', obtain_auth_token)
]
