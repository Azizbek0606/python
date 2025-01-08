from django.contrib import admin
from django.utils.html import format_html
from .models import Logo

class Display_logo(admin.ModelAdmin):
    list_display = ('logo', )

    def logo_tag(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="height: 50px;"/>', obj.logo.url)
        return "No Logo"
    logo_tag.short_description = "Logo"

admin.site.register(Logo, Display_logo)
