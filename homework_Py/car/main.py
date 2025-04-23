from cars import Car
from methods import CarModelSelector, CarSelector, ColorSelector, PaymentProcessor

cars = {
    "sedan": {
        "Toyota Camry": 30000,
        "Honda Accord": 28000,
        "Hyundai Sonata": 27000,
    },
    "hatchback": {
        "Volkswagen Golf": 25000,
        "Ford Focus": 22000,
        "Mazda 3": 23000,
    },
    "coupe": {
        "BMW 4 Series": 45000,
        "Audi A5": 43000,
        "Chevrolet Camaro": 37000,
    },
    "minivan": {
        "Chrysler Pacifica": 35000,
        "Honda Odyssey": 34000,
        "Toyota Sienna": 36000,
    },
    "SUV": {
        "Toyota RAV4": 32000,
        "Honda CR-V": 31000,
        "Ford Explorer": 40000,
    },
}

print("========================================")
print("  Welcome to the Car Selection Program     ")
print("========================================\n")

model_selector = CarModelSelector(cars)
selected_model = model_selector.select_model()

car_selector = CarSelector(cars, selected_model)
selected_car_name, selected_car_price = car_selector.select_car()

color_selector = ColorSelector()
selected_color = color_selector.choose_color()

car = Car(
    model=selected_model,
    name=selected_car_name,
    price=selected_car_price,
    color=selected_color,
)

print("\n========================================")
print("            Review Details              ")
print("========================================")
print(car)
print("========================================")
print("Do you want to buy the car?\n\n1 - Yes\n2 - No")
if model_selector.input_number("\nChoose 1 or 2: ", 2) == 1:
    print("\n========================================")
    print("          Select Payment Method         ")
    print("========================================")
    print("1 - Cash\n2 - Card")
    payment_choice = model_selector.input_number("\nChoose 1 or 2: ", 2)
    payment_method = "Cash" if payment_choice == 1 else "Card"

    payment_processor = PaymentProcessor()
    payment_processor.confirm_payment(car, payment_method)
else:
    print("\nOperation Canceled!")
