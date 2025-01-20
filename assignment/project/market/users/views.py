from django.contrib.auth import authenticate, login , logout
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from orders.models import Order , OrderDetail
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


def singup_view(request):
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
            if user is not None:
                login(request, user)
            return redirect("/")

    return render(request, "registrate/registor.html")


def logout_view(request):
    logout(request)
    return redirect("/registrations")


@login_required
def profile(request):
    request_user = Users.objects.get(user=request.user)
    user_order = Order.objects.filter(customer=request_user)
    order_details = OrderDetail.objects.filter(order__in=user_order)

    pending_orders = order_details.filter(order__status="pending")
    processing_orders = order_details.filter(order__status="processing")
    completed_orders = order_details.filter(order__status="completed")
    cancelled_orders = order_details.filter(order__status="cancelled")

    data = {
        "pending_orders": pending_orders,
        "processing_orders": processing_orders,
        "completed_orders": completed_orders,
        "cancelled_orders": cancelled_orders,
        "user": request_user,
    }
    return render(request, "user_page.html", context=data)
