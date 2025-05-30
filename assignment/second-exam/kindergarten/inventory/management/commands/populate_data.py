from django.core.management.base import BaseCommand
import random
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib.auth.models import User
from inventory.models import Ingredient, Meal, Recipe, Serving, UserRole, Report, PortionEstimate

class Command(BaseCommand):
    help = 'Populates the database with mock data'

    def handle(self, *args, **options):
        users = []
        roles = ['admin', 'chef', 'manager']
        for i in range(1, 6):
            user = User.objects.create_user(
                username=f'user{i}',
                password=f'password{i}',
                first_name=f'First{i}',
                last_name=f'Last{i}',
                email=f'user{i}@example.com'
            )
            role = UserRole.objects.create(
                user=user,
                role=random.choice(roles)
            )
            users.append(user)
            self.stdout.write(self.style.SUCCESS(f"Created user: {user.username} with role {role.role}"))

        # Create ingredients
        ingredients = [
            {"name": "Rice", "min_quantity": 5000},
            {"name": "Chicken", "min_quantity": 3000},
            {"name": "Beef", "min_quantity": 2000},
            {"name": "Potatoes", "min_quantity": 4000},
            {"name": "Carrots", "min_quantity": 2000},
            {"name": "Onions", "min_quantity": 3000},
            {"name": "Tomatoes", "min_quantity": 2500},
            {"name": "Cucumbers", "min_quantity": 1500},
            {"name": "Flour", "min_quantity": 3500},
            {"name": "Eggs", "min_quantity": 1000},
        ]

        ingredient_objs = []
        for ing in ingredients:
            days_ago = random.randint(1, 30)
            obj = Ingredient.objects.create(
                name=ing["name"],
                quantity=random.uniform(ing["min_quantity"] * 1.5, ing["min_quantity"] * 3),
                delivery_date=timezone.now() - timedelta(days=days_ago),
                min_quantity=ing["min_quantity"]
            )
            ingredient_objs.append(obj)
            self.stdout.write(self.style.SUCCESS(f"Created ingredient: {obj.name} ({obj.quantity}g)"))

        # Create meals
        meals = [
            {"name": "Plov", "type": "nonushta"},
            {"name": "Manti", "type": "nonushta"},
            {"name": "Shashlik", "type": "nonushta"},
            {"name": "Lagman", "type": "nonushta"},
            {"name": "Somsa", "type": "nonushta"},
            {"name": "Omelette", "type": "ushta"},
            {"name": "Porridge", "type": "ushta"},
            {"name": "Sandwich", "type": "ushta"},
        ]

        meal_objs = []
        for m in meals:
            obj = Meal.objects.create(
                name=m["name"],
                type=m["type"]
            )
            meal_objs.append(obj)
            self.stdout.write(self.style.SUCCESS(f"Created meal: {obj.name} ({obj.type})"))

        # Create recipes (assign ingredients to meals)
        for meal in meal_objs:
            # Select 3-7 random ingredients for each meal
            num_ingredients = random.randint(3, 7)
            selected_ingredients = random.sample(ingredient_objs, num_ingredients)
            
            for ing in selected_ingredients:
                # Determine quantity based on ingredient type
                if ing.name in ["Rice", "Flour", "Potatoes"]:
                    quantity = random.uniform(100, 500)
                elif ing.name in ["Chicken", "Beef"]:
                    quantity = random.uniform(50, 300)
                else:
                    quantity = random.uniform(20, 150)
                    
                Recipe.objects.create(
                    meal=meal,
                    ingredient=ing,
                    quantity=quantity
                )
                self.stdout.write(self.style.SUCCESS(f"Created recipe: {meal.name} with {ing.name} ({quantity}g)"))

        # Create servings (covering last 3 months)
        now = timezone.now()
        for i in range(90):  # Last 90 days
            date = now - timedelta(days=i)
            # Create 5-15 servings per day
            for _ in range(random.randint(5, 15)):
                meal = random.choice(meal_objs)
                user = random.choice(users)
                
                Serving.objects.create(
                    meal=meal,
                    user=user,
                    date_served=date,
                    portion_count=random.randint(1, 5)
                )
            self.stdout.write(self.style.SUCCESS(f"Created servings for {date.strftime('%Y-%m-%d')}"))

        # Create monthly reports (for last 12 months)
        for i in range(12):
            month = now.replace(day=1) - timedelta(days=30*i)
            for meal in meal_objs:
                prepared = random.randint(50, 300)
                possible = prepared + random.randint(-20, 50)
                difference = ((prepared - possible) / possible) * 100 if possible > 0 else 0
                
                Report.objects.create(
                    month=month,
                    meal=meal,
                    prepared_portions=prepared,
                    possible_portions=possible,
                    difference_percentage=difference,
                    warning_triggered=difference < -10
                )
            self.stdout.write(self.style.SUCCESS(f"Created reports for {month.strftime('%Y-%m')}"))

        # Create portion estimates
        for meal in meal_objs:
            # Get all recipes for this meal
            recipes = Recipe.objects.filter(meal=meal)
            
            # Calculate possible portions based on ingredient quantities
            min_portions = None
            for recipe in recipes:
                # Get the ingredient
                ing = recipe.ingredient
                # Calculate how many portions we can make with this ingredient
                portions = int(ing.quantity / recipe.quantity)
                if min_portions is None or portions < min_portions:
                    min_portions = portions
            
            if min_portions is not None:
                PortionEstimate.objects.create(
                    meal=meal,
                    possible_portions=max(0, min_portions)
                )
                self.stdout.write(self.style.SUCCESS(f"Created portion estimate for {meal.name}: {min_portions} portions"))