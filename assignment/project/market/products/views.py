from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .models import Product, Category

# Create your views here.


def home(request):
    products = Product.objects.all()
    data = {"products": products}
    return render(request, "home.html", context=data)


def product_detail(request, id):
    product = Product.objects.get(id=id)
    data = {"product": product}
    return render(request, "product_detail.html", context=data)


def is_admin(request):
    return request.is_staff


@user_passes_test(is_admin)
def create_product(request):
    if request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        price = request.POST["price"]
        quantity = request.POST["quantity"]
        category_id = request.POST["category"]
        image = request.FILES.get("image")
        category = Category.objects.get(id=category_id)
        product = Product(
            name=name,
            price=price,
            quantity=quantity,
            description=description,
            image=image,
            category=category,
        )
        messages.success(request, "Product created successfully.")
        product.save()
        return render(request, "admin/create_product.html")

    category = Category.objects.all()
    data = {"category": category}
    return render(request, "admin/create_product.html", context=data)


@user_passes_test(is_admin)
def remove_product_page(request):
    products = Product.objects.all()
    data = {"products": products}
    return render(request, "admin/remove_product.html", context=data)


@user_passes_test(is_admin)
def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    messages.success(request, "Product deleted successfully.")
    return redirect("/remove-product/")


@user_passes_test(is_admin)
def update_product(request, id):
    product = Product.objects.get(id=id)

    if request.method == "POST":
        product.name = request.POST["name"]
        product.description = request.POST["description"]
        product.price = request.POST["price"]
        product.quantity = request.POST["quantity"]
        category_id = request.POST["category"]
        product.image = request.FILES.get("image") or product.image

        product.category = Category.objects.get(id=category_id)
        product.save()
        messages.success(request, "Product updated successfully.")
        return redirect("/remove-product/")

    category = Category.objects.all()
    data = {"product": product, "category": category}
    return render(request, "admin/update_product.html", context=data)
