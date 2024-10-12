from django.urls import path
from appburger.views import *


urlpatterns = [
    path('', Market, name='market'),
    path('products/<int:pk>', burger_detail, name='burger_detail'),
    path('success/', order_success, name='order_success'),
    path('products/<int:pk>/submit/', submit_order, name='submit_order'),



]
