from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Book)
admin.site.register(Journal)
admin.site.register(DigitalMedia)
admin.site.register(Notifications)