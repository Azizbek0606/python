from django.contrib import admin
from .models import Ingredient, Meal, Recipe, Serving, UserRole, Report


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "quantity", "delivery_date", "min_quantity")
    search_fields = ("name",)
    list_filter = ("delivery_date",)


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("meal", "ingredient", "quantity")
    search_fields = ("meal__name", "ingredient__name")
    list_filter = ("meal", "ingredient")


@admin.register(Serving)
class ServingAdmin(admin.ModelAdmin):
    list_display = ("meal", "user", "date_served", "portion_count")
    search_fields = ("meal__name", "user__username")
    list_filter = ("date_served", "meal", "user")


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ("user", "role")
    search_fields = ("user__username",)
    list_filter = ("role",)


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = (
        "meal",
        "month",
        "prepared_portions",
        "possible_portions",
        "difference_percentage",
        "warning_triggered",
    )
    search_fields = ("meal__name",)
    list_filter = ("month", "warning_triggered")
