from django.urls import path
from appTwo import views

# user creates his own urls

urlpatterns =[
    path('',views.users,name='users'),
]
