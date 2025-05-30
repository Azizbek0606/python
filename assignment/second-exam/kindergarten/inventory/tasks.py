from celery import shared_task
from django.db.models import Sum
from django.utils import timezone
from django.core.cache import cache
from .models import Meal, Serving, Report, PortionEstimate
from datetime import datetime


@shared_task
def generate_monthly_report():
    today = timezone.now()
    month_start = today.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    month_key = month_start.strftime("%Y-%m")

    for meal in Meal.objects.all():
        # Kesh kaliti
        cache_key = f"report_{meal.id}_{month_key}"
        cached_report = cache.get(cache_key)
        if cached_report:
            continue  # Keshdan foydalanish

        # Oylik tayyorlangan porsiyalar
        prepared_portions = (
            Serving.objects.filter(
                meal=meal,
                date_served__gte=month_start,
                date_served__lt=month_start + timezone.timedelta(days=31),
            ).aggregate(total=Sum("portion_count"))["total"]
            or 0
        )

        # Mumkin bo‘lgan porsiyalarni hisoblash
        min_portions = float("inf")
        for recipe in meal.recipes.all():
            if recipe.quantity > 0:
                portions = recipe.ingredient.quantity // recipe.quantity
                min_portions = min(min_portions, portions)

        # Farq foizini hisoblash
        difference_percentage = 0
        if possible_portions := min_portions:
            difference_percentage = (
                (possible_portions - prepared_portions) / possible_portions
            ) * 100

        # Hisobotni yangilash yoki yaratish
        report, _ = Report.objects.update_or_create(
            meal=meal,
            month=month_start,
            defaults={
                "prepared_portions": prepared_portions,
                "possible_portions": possible_portions,
                "difference_percentage": difference_percentage,
                "warning_triggered": difference_percentage > 15,
            },
        )

        # Keshga saqlash (30 kun)
        cache.set(
            cache_key,
            {
                "prepared_portions": prepared_portions,
                "possible_portions": possible_portions,
                "difference_percentage": difference_percentage,
                "warning_triggered": difference_percentage > 15,
            },
            timeout=2592000,
        )


@shared_task
def update_portion_estimates():
    for meal in Meal.objects.all():
        # Kesh kaliti
        cache_key = f"portion_estimate_{meal.id}"
        cached_estimate = cache.get(cache_key)
        if cached_estimate:
            continue  # Keshdan foydalanish

        min_portions = float("inf")
        for recipe in meal.recipes.all():
            if recipe.quantity > 0:
                portions = recipe.ingredient.quantity // recipe.quantity
                min_portions = min(min_portions, portions)

        # PortionEstimate modelida yangilash yoki yaratish
        estimate, _ = PortionEstimate.objects.update_or_create(
            meal=meal,
            defaults={
                "possible_portions": int(min_portions),
            },
        )

        # Keshga saqlash (1 kun)
        cache.set(cache_key, {"possible_portions": int(min_portions)}, timeout=86400)
