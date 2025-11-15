# from abc import ABC, abstractmethod

# class EmailService:
#     def send_email(self,to,subject,body):
#         print(f"send email to: {to}")
    
# class OrderProcessor:
#     def process_order(self,order):
#         email_service = EmailService()
#         email_service.send_email(order.user , "order confirmed" , "your order is on the way")
    

# task 1


# class Services(ABC):
#     @abstractmethod
#     def send_message():
#         pass




# class EmailService(Services):
#     def send_message(self):
#         print("message sent via email")

# class SMSService(Services):
#     def send_message(self):
#         print("message sent via SMS") 




# class OrderProcessor:
#     def send_email(self, service:Services):
#         self.service = service
#         self.service.send_message()



# order = OrderProcessor()
# email = EmailService()
# sms = SMSService()
# order.send_email(email)
# order.send_email(sms)




# task 2




# class Logger(ABC):
#     @abstractmethod
#     def log(self):
#         pass



# class FileLogger(Logger):
#     def log(self):
#         print("file logger is working")
    
# class ConsoleLogger(Logger):
#     def log(self):
#         print("Console logger is working")
    


# class PaymentService:
#     def write_log(self, logger:Logger):
#         self.logger = logger
#         self.logger.log()
    

# pay1 = PaymentService()
# file_logger = FileLogger()
# pay1.write_log(file_logger)



# task 3 

# class PaymentGateway(ABC):
#     def pay(self):
#         pass

# class HUMOPay(PaymentGateway):
#     def pay(self):
#         print("pay with HUMO")

# class VISAPay(PaymentGateway):
#     def pay(self):
#         print("Pay With Visa")

# class OrderService:
#     def pay(self, payment:PaymentGateway):
#         self.payment = payment
#         self.payment.pay()

# order = OrderService()
# payment1 = HUMOPay()
# order.pay(payment1)




# /////////////// task 1


class Car:
    def __init__(self):
        self.color = None
        self.engine = None
        self.seats = None
        self.has_gps = None
        self.has_sunroof = None

    def __str__(self):
        return f"color={self.color}, engine={self.engine}, seats={self.seats}, has_gps={self.has_gps}, has_sunroof={self.has_sunroof}"
    

class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_color(self, color):
        self.car.color = color
        return self

    def set_engine(self, engine):
        self.car.engine = engine
        return self

    def set_seats(self, seats):
        self.car.seats = seats
        return self

    def add_gps(self):
        self.car.has_gps = True
        return self

    def add_sunroof(self):
        self.car.has_sunroof = True
        return self

    def build(self):
        return self.car

builder = CarBuilder()
car = (builder.set_color("Red")
       .set_engine("V8")
       .set_seats(4)
       .add_gps()
       .add_sunroof()
       .build())
print(car)



# ////////////// task 2




class House:
    def __init__(self):
        self.windows = None
        self.doors = None
        self.roof = None
        self.has_garage = None
        self.has_garden = None
    
    def __str__(self):
        return f"windows={self.windows}, doors={self.doors}, roof={self.roof}, has_garage={self.has_garage}, has_garden={self.has_garden}"

class HouseBuilder:
    def __init__(self):
        self.house = House()
    
    def set_windows(self, windows):
        self.house.windows = windows
        return self
    
    def set_doors(self, doors):
        self.house.doors = doors
        return self
    
    def set_roof(self, roof):
        self.house.roof = roof
        return self
    
    def add_garage(self, has_garage=False):
        self.house.has_garage = has_garage
        return self
    
    def add_garden(self, has_garden=False):
        self.house.has_garden = has_garden
        return self
    
    def build(self):
        return self.house

builder = HouseBuilder()
house = (builder.set_windows(10)
         .set_doors(2)
         .set_roof("Gable")
         .add_garage()
         .add_garden()
         .build())
print(house)



# ////////////// task 3



class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = None
        self.pepperoni = None
        self.mushrooms = None
        self.bacon = None
    
    def __str__(self):
        return f"size={self.size}, cheese={self.cheese}, pepperoni={self.pepperoni}, mushrooms={self.mushrooms}, bacon={self.bacon}"

class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()
    
    def set_size(self, size):
        self.pizza.size = size
        return self
    
    def add_cheese(self, cheese=True):
        self.pizza.cheese = cheese
        return self
    
    def add_pepperoni(self,pepperoni=True):
        self.pizza.pepperoni = pepperoni
        return self
    
    def add_mushrooms(self, mushrooms=True):
        self.pizza.mushrooms = mushrooms
        return self
    
    def add_bacon(self, bacon=True):
        self.pizza.bacon = bacon
        return self
    
    def build(self):
        return self.pizza

builder = PizzaBuilder()
pizza = (builder.set_size("Large")
         .add_cheese()
         .add_pepperoni()
         .add_mushrooms(True)
         .add_bacon()
         .build())
print(pizza)



# ////////////// task 4



class Computer:
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.ram = None
        self.storage = None
        self.os = None
        self.wifi_enabled = None
    
    def __str__(self):
        return f"cpu={self.cpu}, gpu={self.gpu}, ram={self.ram}, storage={self.storage}, os={self.os}, wifi_enabled={self.wifi_enabled}"
    
class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()
    
    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self
    
    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self
    
    def set_ram(self, ram):
        self.computer.ram = ram
        return self
    
    def set_storage(self, storage):
        self.computer.storage = storage
        return self
    
    def set_os(self, os):
        self.computer.os = os
        return self
    
    def enable_wifi(self, wifi_enabled=True):
        self.computer.wifi_enabled = wifi_enabled
        return self
    
    def build(self):
        return self.computer

builder = ComputerBuilder()
computer = (builder.set_cpu("Intel i7")
            .set_gpu("NVIDIA RTX 3080")
            .set_ram("32GB")
            .set_storage("1TB SSD")
            .set_os("Windows 11")
            .enable_wifi()
            .build())
print(computer)



# ////////////// task 5



class UserProfile:
    def __init__(self):
        self.username = None
        self.email = None
        self.age = None
        self.phone = None
        self.address = None
    
    def __str__(self):  
        return f"username={self.username}, email={self.email}, age={self.age}, phone={self.phone}, address={self.address}"

class UserProfileBuilder:
    def __init__(self):
        self.user_profile = UserProfile()
    
    def set_username(self, username):
        self.user_profile.username = username
        return self
    
    def set_email(self, email):
        self.user_profile.email = email
        return self
    
    def set_age(self, age):
        self.user_profile.age = age
        return self
    
    def set_phone(self, phone):
        self.user_profile.phone = phone
        return self
    
    def set_address(self, address):
        self.user_profile.address = address
        return self
    
    def build(self):
        return self.user_profile

builder = UserProfileBuilder()
user_profile = (builder.set_username("john_doe")
                .set_email("email@gmail.com")
                .set_age(30)
                .set_phone("123-456-7890")
                .set_address("123 Main St, Anytown, USA")
                .build())
print(user_profile)



