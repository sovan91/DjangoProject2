from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from appThree import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('users/',include('appThree.urls')),
]
