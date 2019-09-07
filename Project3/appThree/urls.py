from django.urls import path
#from django.conf.urls import include
from appThree import views
#from django.contrib import admin


urlpatterns = [
    path('',views.users,name='users'),
]