from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    IngredientViewSet,
    MealViewSet,
    RecipeViewSet,
    ServingViewSet,
    ReportViewSet,
    LoginView,
    RegisterView,
    LogoutView,
)

router = DefaultRouter()
router.register(r"ingredients", IngredientViewSet, basename="ingredient")
router.register(r"meals", MealViewSet, basename="meal")
router.register(r"recipes", RecipeViewSet, basename="recipe")
router.register(r"servings", ServingViewSet, basename="serving")
router.register(r"reports", ReportViewSet, basename="report")

urlpatterns = [
    path("", include(router.urls)),
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
