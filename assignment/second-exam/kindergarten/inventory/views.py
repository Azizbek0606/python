from django.shortcuts import render
from django.db import transaction
from django.db.models import F
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Ingredient, Meal, Recipe, Serving, UserRole, Report, PortionEstimate
from .serializers import (
    IngredientSerializer,
    MealSerializer,
    RecipeSerializer,
    ServingSerializer,
    ReportSerializer,
    LoginSerializer,
    UserSerializer,
    PortionEstimateSerializer,
)
from .permissions import IsAdminOrManager


# Frontend sahifalari uchun view funksiyalar
def index(request):
    return render(request, "index.html")


def meals(request):
    return render(request, "meals.html")


def serve_meal(request):
    return render(request, "serve_meal.html")


def reports(request):
    return render(request, "reports.html")


# Ingredient ViewSet
def ingredients(request):
    return render(request, "ingredients.html")


# Ingredient ViewSet
class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsAdminOrManager()]
        return [IsAuthenticated()]

    @action(detail=False, methods=["get"])
    def low_stock(self, request):
        low_stock_ingredients = Ingredient.objects.filter(
            quantity__lte=F("min_quantity")
        )
        serializer = self.get_serializer(low_stock_ingredients, many=True)
        return Response(serializer.data)


# Meal ViewSet
class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["get"])
    def by_type(self, request):
        meals = Meal.objects.values("type").annotate(
            portions=Sum("servings__portion_count")
        )
        return Response(meals)


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["meal"]

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsAdminOrManager()]
        return [IsAuthenticated()]


class ServingViewSet(viewsets.ModelViewSet):
    queryset = Serving.objects.all()
    serializer_class = ServingSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ["create", "serve_meal"]:
            return [IsAuthenticated(), IsAdminOrChef()]
        return [IsAuthenticated()]

    @action(detail=False, methods=["post"])
    def serve_meal(self, request):
        meal_id = request.data.get("meal_id")
        portion_count = int(request.data.get("portion_count", 1))
        try:
            meal = Meal.objects.get(id=meal_id)
            with transaction.atomic():
                for recipe in meal.recipes.all():
                    ingredient = recipe.ingredient
                    required_quantity = recipe.quantity * portion_count
                    if ingredient.quantity < required_quantity:
                        return Response(
                            {
                                "error": f"{ingredient.name} yetarli emas. Mavjud: {ingredient.quantity}g, Talab qilinadi: {required_quantity}g"
                            },
                            status=status.HTTP_400_BAD_REQUEST,
                        )
                    ingredient.quantity -= required_quantity
                    ingredient.save()
                Serving.objects.create(
                    meal=meal, user=request.user, portion_count=portion_count
                )
            return Response(
                {"message": "Ovqat muvaffaqiyatli berildi"},
                status=status.HTTP_201_CREATED,
            )
        except Meal.DoesNotExist:
            return Response(
                {"error": "Ovqat topilmadi"}, status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=False, methods=["get"])
    def portion_estimate(self, request):
        meal_id = request.query_params.get("meal_id")
        try:
            meal = Meal.objects.get(id=meal_id)
            min_portions = float("inf")
            for recipe in meal.recipes.all():
                ingredient = recipe.ingredient
                if recipe.quantity > 0:
                    portions = ingredient.quantity // recipe.quantity
                    min_portions = min(min_portions, portions)
            return Response({"meal": meal.name, "possible_portions": int(min_portions)})
        except Meal.DoesNotExist:
            return Response(
                {"error": "Ovqat topilmadi"}, status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=False, methods=["get"])
    def by_user(self, request):
        servings = Serving.objects.values("user__username").annotate(
            total_portions=Sum("portion_count")
        )
        return Response(servings)

    @action(detail=False, methods=["get"])
    def by_date(self, request):
        servings = (
            Serving.objects.values("date_served__year", "date_served__month")
            .annotate(total_portions=Sum("portion_count"))
            .order_by("date_served__year", "date_served__month")
        )
        return Response(servings)


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsAdminOrManager()]
        return [IsAuthenticated()]

    @action(detail=False, methods=["get"])
    def warnings(self, request):
        warnings = (
            Report.objects.filter(warning_triggered=True)
            .values("meal__name")
            .annotate(count=Sum("warning_triggered"))
        )
        return Response(warnings)


class PortionEstimateViewSet(viewsets.ModelViewSet):
    queryset = PortionEstimate.objects.all()
    serializer_class = PortionEstimateSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsAdminOrManager()]
        return [IsAuthenticated()]


def login_page(request):
    return render(request, "login.html")


def logout_page(request):
    return render(request, "logout.html")


def register_page(request):
    return render(request, "register.html")


class LoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        # Django session uchun login
        login(request, user)
        # Token yaratish
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
                "username": user.username,
                "role": user.role.role if hasattr(user, "role") else "user",
            }
        )


class RegisterView(APIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            if User.objects.filter(username=username).exists():
                return Response(
                    {"error": "Bu foydalanuvchi nomi allaqachon mavjud"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # Foydalanuvchi yaratish
            user = User.objects.create_user(username=username, password=password)
            # Manager roli qo‘shish
            UserRole.objects.create(user=user, role="manager")
            # Django session uchun login
            login(request, user)
            # Token yaratish
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "token": token.key,
                    "username": user.username,
                    "role": user.role.role if hasattr(user, "role") else "user",
                    "message": "Foydalanuvchi muvaffaqiyatli ro‘yxatdan o‘tdi",
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            if User.objects.filter(username=username).exists():
                return Response(
                    {"error": "Bu foydalanuvchi nomi allaqachon mavjud"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            user = User.objects.create_user(username=username, password=password)
            UserRole.objects.create(user=user, role="manager")
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "token": token.key,
                    "username": user.username,
                    "message": "Foydalanuvchi muvaffaqiyatli ro‘yxatdan o‘tdi",
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Tokenni o‘chirish
            request.user.auth_token.delete()
            # Sessionni tozalash
            logout(request)
            return Response(
                {"message": "Muvaffaqiyatli chiqildi"}, status=status.HTTP_200_OK
            )
        except Token.DoesNotExist:
            return Response(
                {"error": "Token topilmadi"}, status=status.HTTP_400_BAD_REQUEST
            )


# Ruxsatlarni tekshirish uchun maxsus permission class
from rest_framework.permissions import BasePermission


class IsAdminOrManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.role.role in ["admin", "manager"]
            if hasattr(request.user, "role")
            else False
        )


class IsAdminOrChef(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.role.role in ["admin", "chef"]
            if hasattr(request.user, "role")
            else False
        )
