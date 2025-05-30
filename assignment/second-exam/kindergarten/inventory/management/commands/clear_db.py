from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from inventory.models import Ingredient, Meal, Recipe, Serving, UserRole, Report


class Command(BaseCommand):
    help = "Ma'lumotlar bazasidagi barcha ma'lumotlarni tozalash"

    def add_arguments(self, parser):
        parser.add_argument(
            "--confirm",
            action="store_true",
            help="Tozalashni tasdiqlash",
        )

    def handle(self, *args, **options):
        if not options["confirm"]:
            self.stdout.write(
                self.style.WARNING(
                    """
Ehtiyot bo'ling! Bu komanda BAZADAGI BARCHA MA'LUMOTLARNI O'CHIRIB TASHLAYDI!
Agar ishonchingiz komil bo'lsa, --confirm flagini qo'shing:
python manage.py db_tozalash --confirm
                """
                )
            )
            return

        # Modellarni tozalash tartibi (foreign key bog'liqliklarini hisobga olgan holda)
        models_to_clear = [
            Serving,
            Report,
            Recipe,
            UserRole,
            Ingredient,
            Meal,
            User,
        ]

        for model in models_to_clear:
            count, _ = model.objects.all().delete()
            self.stdout.write(
                self.style.SUCCESS(
                    f"{model.__name__} jadvalidan {count} ta yozuv o'chirildi"
                )
            )

        self.stdout.write(
            self.style.SUCCESS("Barcha jadvallar muvaffaqiyatli tozalandi!")
        )
