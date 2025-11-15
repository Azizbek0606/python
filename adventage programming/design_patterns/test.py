import unittest

# class Burger:
#     def __init__(self):
#         self.bun = None
#         self.patty = None
#         self.cheese = None
#         self.toppings = []
#         self.sauces = []


#     def price(self):
#         base_price = 5.0
#         return base_price + 0.5 * len(self.toppings) + 0.25 * len(self.sauces)

#     def __str__(self):
#         return f"bun={self.bun}, patty={self.patty}, cheese={self.cheese}, toppings={self.toppings}, sauces={self.sauces}, price=${self.price():.2f}"
    
# class BurgerBuilder:
#     def __init__(self):
#         self.burger = Burger()
    
#     def set_bun(self, bun):
#         self.burger.bun = bun
#         return self
    
#     def set_patty(self, patty):
#         self.burger.patty = patty
#         return self
    
#     def add_cheese(self, cheese=True):
#         self.burger.cheese = cheese
#         return self
    
#     def add_topping(self, topping):
#         self.burger.toppings.append(topping)
#         return self
    
#     def add_sauce(self, sauce):
#         self.burger.sauces.append(sauce)
#         return self
    
#     def build(self):
#         if not self.burger.bun or not self.burger.patty:
#             raise ValueError("Bun and patty must be set")
#         return self.burger

# def test_burger_builder():
#     builder = BurgerBuilder()
#     burger = (builder.set_bun("Sesame")
#               .set_patty("Beef")
#               .add_cheese()
#               .add_topping("Lettuce")
#               .add_topping("Tomato")
#               .add_sauce("Ketchup")
#               .add_sauce("Mayo")
#               .build())
#     print(burger)
#     assert burger.bun == "Sesame"
#     assert burger.patty == "Beef"
#     assert burger.cheese is True
#     assert burger.toppings == ["Lettuce", "Tomato"]
#     assert burger.sauces == ["Ketchup", "Mayo"]
#     assert abs(burger.price() - 6.5) < 5





# class Computer:
#     def __init__(self):
#         self.cpu = None
#         self.gpu = None
#         self.ram = None
#         self.storage = None
#         self.os = None
    
#     def __str__(self):
#         return f"cpu={self.cpu}, gpu={self.gpu}, ram={self.ram}, storage={self.storage}, os={self.os}"

# class ComputerBuilder:
#     def __init__(self):
#         self.computer = Computer()
    
#     def set_cpu(self, cpu):
#         self.computer.cpu = cpu
#         return self
    
#     def set_gpu(self, gpu):
#         self.computer.gpu = gpu
#         return self
    
#     def set_ram(self, ram):
#         self.computer.ram = ram
#         return self
    
#     def set_storage(self, storage):
#         self.computer.storage = storage
#         return self
    
#     def set_os(self, os):
#         self.computer.os = os
#         return self
    
#     def build(self):
#         return self.computer

# class TestComputerBuilder(unittest.TestCase):
#     def test_all_attributes_set(self):
#         builder = ComputerBuilder()
#         computer = (builder.set_cpu("Intel i7")
#                     .set_gpu("NVIDIA RTX 3080")
#                     .set_ram(32)
#                     .set_storage(1000)
#                     .set_os("Windows 11")
#                     .build())
#         self.assertEqual(computer.cpu, "Intel i7")
#         self.assertEqual(computer.gpu, "NVIDIA RTX 3080")
#         self.assertEqual(computer.ram, 32)
#         self.assertEqual(computer.storage, 1000)
#         self.assertEqual(computer.os, "Windows 11")
    
#     def test_chaining_methods(self):
#         builder = ComputerBuilder()
#         computer = (builder.set_cpu("AMD Ryzen 9")
#                     .set_ram(64)
#                     .set_storage(2000)
#                     .build())
#         self.assertEqual(computer.cpu, "AMD Ryzen 9")
#         self.assertEqual(computer.ram, 64)
#         self.assertEqual(computer.storage, 2000)
#         self.assertIsNone(computer.gpu)
#         self.assertIsNone(computer.os)
    
#     def test_missing_fields(self):
#         builder = ComputerBuilder()
#         computer = builder.build()
#         self.assertIsNone(computer.cpu)
#         self.assertIsNone(computer.gpu)
#         self.assertIsNone(computer.ram)
#         self.assertIsNone(computer.storage)
#         self.assertIsNone(computer.os)





class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Product:
    def __init__(self, price, title):
        self.price = price
        self.title = title

    
class OrderItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
    
    
class Order:
    order_list = []
    def __init__(self, owner, order_item):
        self.owner = owner
        self.order_item = order_item
        
    def order_list_append(self):
        self.order_list.append(self)
    
    def total_price(self):
        total = 0
        for order in self.order_list:
            total += order.order_item.product.price * order.order_item.quantity
        return total


class TestOrderSystem(unittest.TestCase):
    def test_user_attributes(self):
        user = User("John", "Doe")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
    def test_product_attributes(self):
        product = Product(10.0, "Widget")
        self.assertEqual(product.price, 10.0)
        self.assertEqual(product.title, "Widget")
    def test_order_item_attributes(self):
        product = Product(15.0, "Gadget")
        order_item = OrderItem(product, 2)
        self.assertEqual(order_item.product, product)
        self.assertEqual(order_item.quantity, 2)
    def test_order_total_price(self):
        user = User("Alice", "Smith")
        product1 = Product(20.0, "Thingamajig")
        product2 = Product(30.0, "Doohickey")
        order_item1 = OrderItem(product1, 1)
        order_item2 = OrderItem(product2, 3)
        order1 = Order(user, order_item1)
        order2 = Order(user, order_item2)
        order1.order_list_append()
        order2.order_list_append()
        self.assertEqual(order1.total_price(), 20.0 + 30.0 * 3)
