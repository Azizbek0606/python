from django.urls import path
from .views import *

app_name='orders'

urlpatterns = [
    path("", orders, name="orders"),
    path("orders/<id>", create_order, name="create_order"),
    path("change-status/<order_id>", change_status, name="change_status"),
]
