# class LivingBeing:
#     def __init__(self, name):
#         self.name = name
        
#     def set_bug(self):
#         return 2 / 0

# class Animal(LivingBeing):
#     def __init__(self, name, species):
#         super().__init__(name)
    
#     def breath(self):
#         return f"{self.name} is breathing."
    
# class Mammal(Animal):
#     def __init__(self, name, species):
#         super().__init__(name, species)
    
#     def walk(self):
#         return f"{self.name} is walking on two legs."

# class Human(Mammal):
#     def __init__(self, name, species, language):
#         super().__init__(name, species)
#         self.language = language
    
#     def speak(self):
#         return f"{self.name} says hello in {self.language}."
    
# human = Human("Alice", "Homo sapiens", "English")

# print(human.set_bug())
# print(human.breath())
# print(human.walk())
# print(human.speak())


# class Employee:
#     def __init__(self, name, base_salary):
#         self.name = name
#         self.base_salary = base_salary
    
#     def calculate_salary(self):
#         return self.base_salary

# class Developer(Employee):

#     def __init__(self, name, base_salary, line_of_code, bug_rate):
#         super().__init__(name, base_salary)
#         self.line_of_code = line_of_code
#         self.bug_rate = bug_rate

#     def calculate_salary(self):
#         return super().calculate_salary()

#     def salary(self):
#         return f"{self.name} - {self.base_salary - (self.line_of_code * 0.5) - (self.base_salary * 50)}"

# class Manager(Employee):
#     def __init__(self, name, base_salary, team_size, bonus_per_member):
#         super().__init__(name, base_salary)
#         self.team_size = team_size
#         self.bonus_per_member = bonus_per_member

#     def calculate_salary(self):
#         return super().calculate_salary()

#     def salary(self):
#         return f"{self.name} - {self.base_salary + (self.team_size * self.bonus_per_member)}"

# dev = Developer("Alice", 5000, 100, 2)
# mgr = Manager("Bob", 7000, 5, 200)
# print(dev.salary())
# print(mgr.salary()) 


# from abc import ABC, abstractmethod

# class Payment(ABC):
#     @abstractmethod
#     def pay(self):
#         pass

# class CreditCardPayment(Payment):
#     def __init__(self, card_number):
#         self.card_number = card_number
    
#     def pay(self):
#         return f"\nPaid with credit card {self.card_number}\n"
    
# class PayPalPayment(Payment):
#     def __init__(self, email):
#         self.email = email
    
#     def pay(self):
#         return f"Paid with PayPal account {self.email}\n"

# class BankTransferPayment(Payment):
#     def __init__(self, account_number):
#         self.account_number = account_number
    
#     def pay(self):
#         return f"Paid with bank transfer from account {self.account_number}\n"

# class PaymentProcess:
#     def __init__(self, payment_method: Payment):
#         self.payment_method = payment_method
    
#     def process_payment(self):
#         return self.payment_method.pay()


# credit_card_payment = CreditCardPayment("1234-5678-9012-3456")
# paypal_payment = PayPalPayment("example@paypal.com")
# bank_transfer_payment = BankTransferPayment("9876543210")

# payment_process1 = PaymentProcess(credit_card_payment)
# payment_process2 = PaymentProcess(paypal_payment)
# payment_process3 = PaymentProcess(bank_transfer_payment)

# print("\n==================================")
# print(payment_process1.process_payment())
# print(payment_process2.process_payment())
# print(payment_process3.process_payment())
# print("==================================\n")

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c

rect = Rectangle(4, 5)
circle = Circle(3)
triangle = Triangle(3, 4, 5)

print(f"Rectangle area: {rect.area()}, perimeter: {rect.perimeter()}")
print(f"Circle area: {circle.area()}, perimeter: {circle.perimeter()}")
print(f"Triangle area: {triangle.area()}, perimeter: {triangle.perimeter()}")