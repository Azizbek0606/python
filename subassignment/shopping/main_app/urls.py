from django.urls import path
from .views import *

app_name = "main_app"

urlpatterns = [
    path("", home, name="home"),
    path("filter/", filter_by_category, name="filter"),
]
