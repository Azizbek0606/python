from django.urls import path
from .views import *

app_name='users'

urlpatterns = [
    path("", login_view, name="login"),
    path("register/", singup_view, name="sign_up"),
    path('logout/', logout_view, name="logout"),
    path('profile/', profile, name="profile")
]
