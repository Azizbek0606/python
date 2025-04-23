class CarModelSelector:
    def __init__(self, cars):
        self.cars = cars

    def select_model(self):
        print("\n========================================")
        print("            Select a Model              ")
        print("========================================")
        models = list(self.cars.keys())
        for index, model in enumerate(models, start=1):
            print(f"{index} - {model}")
        print("========================================")
        choice = self.input_number("\nEnter model ID number: ", len(models))
        return models[choice - 1]

    def input_number(self, prompt, max_num):
        while True:
            selected = input(prompt)
            if selected.isdigit():
                selected = int(selected)
                if 1 <= selected <= max_num:
                    return selected
                print(f"Error: Enter a number between 1 and {max_num}!")
            else:
                print("Enter numbers only!")


class CarSelector:
    def __init__(self, cars, selected_model):
        self.cars = cars[selected_model]
        self.car_price = None

    def select_car(self):
        print("\n========================================")
        print("            Select a Car                ")
        print("========================================")
        cars = list(self.cars.items())
        for index, (car, price) in enumerate(cars, start=1):
            print(f"{index} - {car}: ${price}")
        print("========================================")
        choice = self.input_number("\nEnter car ID number: ", len(cars))
        selected_car, self.car_price = cars[choice - 1]
        return selected_car, self.car_price

    def input_number(self, prompt, max_num):
        while True:
            selected = input(prompt)
            if selected.isdigit():
                selected = int(selected)
                if 1 <= selected <= max_num:
                    return selected
                print(f"Error: Enter a number between 1 and {max_num}!")
            else:
                print("Enter numbers only!")


class ColorSelector:
    def choose_color(self):
        colors = ["Black", "White", "Gray"]
        print("\n========================================")
        print("           Choose a Color               ")
        print("========================================")
        for index, color in enumerate(colors, start=1):
            print(f"{index} - {color}")
        print("========================================")
        choice = self.input_number("\nEnter color ID number: ", len(colors))
        return colors[choice - 1]

    def input_number(self, prompt, max_num):
        while True:
            selected = input(prompt)
            if selected.isdigit():
                selected = int(selected)
                if 1 <= selected <= max_num:
                    return selected
                print(f"Error: Enter a number between 1 and {max_num}!")
            else:
                print("Enter numbers only!")


class PaymentProcessor:
    def confirm_payment(self, car, payment_method):
        print("\n========================================")
        print("          Payment Information          ")
        print("========================================")
        print(
            f"Payment method: {payment_method}\nModel: {car.model}\nCar: {car.name}\nColor: {car.color}\nPrice: ${car.price}\nTotal amount paid: ${car.price}"
        )
        print("========================================\n")
