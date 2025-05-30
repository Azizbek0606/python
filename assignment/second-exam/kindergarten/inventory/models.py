from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    quantity = models.FloatField(validators=[MinValueValidator(0.0)])
    delivery_date = models.DateField()
    min_quantity = models.FloatField(validators=[MinValueValidator(0.0)], default=0.0)

    def __str__(self):
        return f"{self.name} ({self.quantity}g)"

    class Meta:
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"


class Meal(models.Model):
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=50, default="nonushta")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Meal"
        verbose_name_plural = "Meals"


class Recipe(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name="recipes")
    ingredient = models.ForeignKey(
        Ingredient, on_delete=models.CASCADE, related_name="recipes"
    )
    quantity = models.FloatField(validators=[MinValueValidator(0.0)])

    def __str__(self):
        return f"{self.meal.name}: {self.ingredient.name} ({self.quantity}g)"

    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"
        unique_together = ["meal", "ingredient"]


class Serving(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name="servings")
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="servings"
    )
    date_served = models.DateTimeField(auto_now_add=True)
    portion_count = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return f"{self.meal.name} served by {self.user.username if self.user else 'Unknown'} on {self.date_served}"

    class Meta:
        verbose_name = "Serving"
        verbose_name_plural = "Servings"


class UserRole(models.Model):
    ROLE_CHOICES = (
        ("admin", "Admin"),
        ("chef", "Oshpaz"),
        ("manager", "Menejer"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="role")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="chef")

    def __str__(self):
        return f"{self.user.username} - {self.role}"

    class Meta:
        verbose_name = "User Role"
        verbose_name_plural = "User Roles"


class Report(models.Model):
    month = models.DateField()
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name="reports")
    prepared_portions = models.PositiveIntegerField(default=0)
    possible_portions = models.PositiveIntegerField(default=0)
    difference_percentage = models.FloatField(default=0.0)
    warning_triggered = models.BooleanField(default=False)

    def __str__(self):
        return f"Report for {self.meal.name} ({self.month.strftime('%Y-%m')})"

    class Meta:
        verbose_name = "Report"
        verbose_name_plural = "Reports"
        unique_together = [
            "meal",
            "month",
        ]


class PortionEstimate(models.Model):
    meal = models.ForeignKey(
        Meal, on_delete=models.CASCADE, related_name="portion_estimates"
    )
    possible_portions = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.meal.name}: {self.possible_portions} portions"

    class Meta:
        verbose_name = "Portion Estimate"
        verbose_name_plural = "Portion Estimates"
        unique_together = ["meal"]
