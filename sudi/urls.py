from django.contrib import admin
from django.urls import include, path
from members.views import *

urlpatterns = [
    path('', wisata, name='wisata'),
    path('coba', coba, name='coba'),
    path('home', home, name='home'),
    path('base', base, name='base'),
    path('admin/', admin.site.urls),
]