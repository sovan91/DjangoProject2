from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render





def index(request):
    return render(request,'stack/index.html')




def users(request):
    user_list = Users.objects.order_by('Name')
    user_dict = {'users':user_list}
    return render(request,'static/users.html',context=user_dict)

