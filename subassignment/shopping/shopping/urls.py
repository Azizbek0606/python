from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.urls import re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path("if/you/admin/", admin.site.urls),
    path("", include("main_app.urls", namespace="main_app")),
    # re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    # re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
