from django.urls import path
from . import views
app_name = 'main'

urlpatterns = [
    path("", views.home, name="index"),
    path("detail/<id>", views.detail, name="detail"),
    path("administation/", views.admin, name="admin"),
    path("delete/<id>", views.delete, name="delete"),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('register/', views.registerView, name='register'),
]