from faker import Faker
import random

fake = Faker()


def generate_name():
    return fake.name()


def generate_email():
    return fake.email()


def generate_phone_number():
    random_digits = fake.numerify(text="########")
    random_begin_num = ["91", "90", "88", "93", "97", "99"]
    random_index = random.randint(0, len(random_begin_num) - 1)
    return f"{random_begin_num[random_index]}{random_digits}"