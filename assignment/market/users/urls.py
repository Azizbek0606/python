from django.urls import path
from .views import *

app_name='users'

urlpatterns = [
    path("", login_view, name="login"),
    path("register/", sing_up_view, name="sign_up"),
]
