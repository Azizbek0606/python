from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Users

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "registrate/login.html")


def sing_up_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        role = request.POST["role"]
        phone_number = request.POST["phone_number"]

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()

            profile = Users.objects.create(
                user=user, role=role, phone_number=phone_number
            )
            profile.save()

            return redirect("/")

    return render(request, "registrate/registor.html")
