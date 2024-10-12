from django.contrib import admin
from django.urls import path,include
from appburger.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appburger.urls')),
    path('about/', include('about.urls')),
    path('contact/', include('contact.urls')),
    path('market/', include('market.urls')),
    
]

admin.site.index_title = "BurgerBAR"
admin.site.site_header = "BurgerBAR"
admin.site.site_title = "BurgerBAR"