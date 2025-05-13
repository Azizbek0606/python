from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Book, Journal, DigitalMedia, Notifications
def home(request):
    books = Book.objects.all()
    data = {
        "books": books
    }
    return render(request, "index.html", context=data)

def detail(request, id):
    book = Book.objects.get(id=id)
    data = {
        "i": book
    }
    return render(request, "detail.html", context=data)

def admin(request):
    books = Book.objects.all()
    journals = Journal.objects.all()
    digital_media = DigitalMedia.objects.all()
    notifications = Notifications.objects.all()
    data = {
        "books": books,
        "journals": journals,
        "digital_media": digital_media,
        "notifications": notifications
    }
    return render(request, "admin.html", context=data)


def delete(request, id):
    book = Book.objects.filter(id=id)
    book.delete()
    return redirect("http://127.0.0.1:8000/administation/")


def loginView(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")

    return render(request, "login.html")

def logoutView(request):
    logout(request)
    return redirect("/")

def registerView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        login(request, user)
        return redirect("/")

    return render(request, "register.html")
