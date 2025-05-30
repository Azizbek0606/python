from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import Ingredient, Meal, Recipe, Serving, Report, PortionEstimate


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ["id", "name", "quantity", "delivery_date", "min_quantity"]


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ["id", "name", "type"]


class RecipeSerializer(serializers.ModelSerializer):
    ingredient = serializers.StringRelatedField()
    meal = serializers.StringRelatedField()

    class Meta:
        model = Recipe
        fields = ["id", "meal", "ingredient", "quantity"]


class ServingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    meal = serializers.StringRelatedField()

    class Meta:
        model = Serving
        fields = ["id", "meal", "user", "date_served", "portion_count"]


class ReportSerializer(serializers.ModelSerializer):
    meal = serializers.CharField(source="meal.name")  # meal nomini qaytarish

    class Meta:
        model = Report
        fields = [
            "id",
            "meal",
            "month",
            "prepared_portions",
            "possible_portions",
            "difference_percentage",
            "warning_triggered",
        ]


class PortionEstimateSerializer(serializers.ModelSerializer):
    meal = serializers.StringRelatedField()

    class Meta:
        model = PortionEstimate
        fields = ["id", "meal", "possible_portions", "updated_at"]


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError(
                    "Foydalanuvchi nomi yoki parol noto‘g‘ri"
                )
            if not user.is_active:
                raise serializers.ValidationError("Foydalanuvchi faol emas")
        else:
            raise serializers.ValidationError(
                "Foydalanuvchi nomi va parol kiritilishi shart"
            )
        data["user"] = user
        return data


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True, min_length=8)
    confirm_password = serializers.CharField(write_only=True, min_length=8)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        confirm_password = data.get("confirm_password")

        if not username:
            raise serializers.ValidationError(
                {"username": "Foydalanuvchi nomi kiritilishi shart"}
            )
        if not password or not confirm_password:
            raise serializers.ValidationError(
                {"password": "Parol va tasdiqlash paroli kiritilishi shart"}
            )
        if password != confirm_password:
            raise serializers.ValidationError(
                {"confirm_password": "Parollar mos kelmadi"}
            )
        return data
