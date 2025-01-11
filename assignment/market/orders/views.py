from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Q
from users.models import Users
from .models import Order, OrderDetail
from products.models import Product

# Create your views here.


from django.db.models import Q


@login_required
def orders(request):
    request_user = Users.objects.get(user=request.user)
    user_order = Order.objects.filter(customer=request_user).filter(
        Q(status="pending") | Q(status="processing")
    )
    order_details = OrderDetail.objects.filter(order__in=user_order)

    if request.method == 'POST':
        order_id = request.POST.get("order_id")
        quantity = request.POST.get('quantity')
        order = OrderDetail.objects.get(id=order_id)
        order.upadate_quantity(quantity)

    data = {"order": order_details}
    return render(request, "orders/orders.html", context=data)


@login_required
def create_order(request, id):
    product = Product.objects.get(id=id)

    order, created = Order.objects.get_or_create(
        customer=request.user.profile,
        status="pending",
    )

    order_detail, detail_created = OrderDetail.objects.get_or_create(
        order=order,
        product=product,
        defaults={"quantity": 1, "price": product.price},
    )

    if not detail_created:
        order_detail.quantity += 1
        order_detail.save()

    return redirect("/", order_id=order.id)
