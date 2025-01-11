from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    path("", home, name="home"),
    path("create/", create_product, name="create"),
    path("remove-product/", remove_product_page, name="remove_product"),
    path("details/<id>", product_detail, name="details"), 
    path("delete/<id>", delete_product, name="delete"),
    path("update/<id>", update_product, name="update"),
]
