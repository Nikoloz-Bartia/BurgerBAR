from django.urls import path
from appburger.views import *


urlpatterns = [
    path('', Contact, name='contact'),
    
]