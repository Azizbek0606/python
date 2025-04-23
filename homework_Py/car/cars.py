class Car:
    def __init__(self, model, name, price, color=None):
        self.model = model
        self.name = name
        self.price = price
        self.color = color

    def __str__(self):
        return f"Model: {self.model},\nName: {self.name},\nPrice: ${self.price},\nColor: {self.color or 'Not Selected'}"
