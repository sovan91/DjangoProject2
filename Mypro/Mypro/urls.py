
from django.contrib import admin
from django.urls import path
from appTwo import views
from django.conf.urls import include
#urls patterns linking######


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('users/',include('appTwo.urls')),
]
