from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path
from django.conf import settings
from inventory.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("ingredients/", ingredients, name="ingredients"),
    path("login/", login_page, name="login"),
    path("logout/", logout_page, name="login"),
    path("register/", register_page, name="register"),
    path("meals/", meals, name="meals"),
    path("serve_meal/", serve_meal, name="serve_meal"),
    path("reports/", reports, name="reports"),
    path("api/", include("inventory.urls")),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]
