from django.shortcuts import render
from users.models import Users
# Create your views here.


def home(request):
    users = Users.objects.all()
    data = {
        "user_status":users
    } 
    return render(request, 'home.html' , context=data)