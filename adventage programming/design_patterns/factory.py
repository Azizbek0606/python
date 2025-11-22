from abc import ABC, abstractmethod
# class MessageFactory:

#     def choose_class(self, param, message):
#         if param == "email":
#             EmailNotifire().send_message(message)
#         elif param == "sms":
#             SMSNotifier().send_message(message)
#         elif param == "push":
#             PushNotifire().send_message(message)
#         else:
#             print("Wrong param!")
        

# class EmailNotifire:
#     def send_message(self, message):
#         print(f"class Email, message: {message}")
    
# class SMSNotifier:
#     def send_message(self,message):
#         print(f"calss SMS, Message: {message}")
    
# class PushNotifire:
#     def send_message(self, message):
#         print(f"class Push, message: {message}")



# # test:

# f1 = MessageFactory()
# f1.choose_class("sms", "send email with 'email' ")




# from abc import ABC, abstractmethod
# class ShapeCreator(ABC):
#     @abstractmethod
#     def draw(self):
#         pass


# class Circle(ShapeCreator):
#     def draw(self):
#         print("circle creator working ! ")

# class Square(ShapeCreator):
#     def draw(self):
#         print("Square creator working ! ")
    
# class Triangle(ShapeCreator):
#     def draw(self):
#         print("Triangle creator working ! ")

# class ShapeFactory:
#     def create(self, param):
#         if param == "circle":
#             Circle().draw()
#         elif param == "triangle":
#             Triangle().draw()
#         elif param == "square":
#             Square().draw()
#         else:
#             print(f"{param} not found use: ciecle, triangle, square")
        
# # test:

# shape1 = ShapeFactory()
# shape1.create("square")
# shape1.create("triangle")
# shape1.create("circle")
# shape1.create("wrong param")
# bir turgdagi bir biriga o'xshash bo'lgan prodductlarni create qilish imkoniyatiga ega

# class TransportSelector:
#     def decision(self, type):
#         if type == "road":
#             Truck.deliver()
#         elif type == "sea":
#             Ship.deliver()
#         elif type == "air":
#             Airplane.deliver()
#         else:
#             print("type not found !!!")


# class Truck:
#     def deliver():
#         print("Truck factiry")

# class Ship:
#     def deliver():
#         print("ship factory")
    
# class Airplane:
#     def deliver():
#         print("aeroplan factory")


# product1 = TransportSelector()
# product1.decision("road")
# product1.decision("air")
# product1.decision("sea")




# class PizzaStore(ABC):
#     @abstractmethod
#     def pizza():
#         pass


# class ChicagoPizzaStore(PizzaStore):
#     def pizza():
#         ChicagoCheesePizza()

# class NYPizzaStore(PizzaStore):
#     def pizza():
#         NYCheesePizza()


# class PizzaBuilder(ABC):
#     @abstractmethod
#     def build_pizza():
#         pass

# class NYCheesePizza(PizzaBuilder):
#     def build_pizza():
#         print("building NY Cheese Pizza")
    
# class ChicagoCheesePizza(PizzaBuilder):
#     def build_pizza():
#         print("building Chicago Cheese Pizza")
    


# class Client:
#     def __init__(self, pizza: PizzaBuilder):
#         self.pizza = pizza.build_pizza()
    
#     def build_pizza(self):
#         return self.pizza




# class DocumentCreatorFactory(ABC):
#     @abstractmethod
#     def create_document(self):
#         pass

# class WordDocumentCreator(DocumentCreatorFactory):
#     def create_document(self):
#         return WordDocument()
    
# class PdfDocumentCreator(DocumentCreatorFactory):
#     def create_document(self):
#         return PdfDocument()
    
# class ExcelDocumentCreator(DocumentCreatorFactory):
#     def create_document(self):
#         return ExcelDocument()


# class DocumentCreator(ABC):
#     @abstractmethod
#     def display(self):
#         pass


# class WordDocument(DocumentCreator):
#     def display(self):
#         print("This is a Word Document")

# class PdfDocument(DocumentCreator):
#     def display(self):
#         print("This is a PDF Document")

# class ExcelDocument(DocumentCreator):
#     def display(self):
#         print("This is an Excel Document")


# class Client:
#     def __init__(self, creator: DocumentCreator):
#         self.creator = creator.display()
    
#     def create_document(self):
#         return self.creator


# word1 = WordDocument()
# excel1 = ExcelDocument()
# pdf1 = PdfDocument()

# document1 = Client(word1)
# document2 = Client(excel1)
# document3 = Client(pdf1)


class UICreator(ABC):
    @abstractmethod
    def button():
        pass

    @abstractmethod
    def checkbox():
        pass

    @abstractmethod
    def window():
        pass


class DarkThemeCreator(UICreator):
    def button():
        print("Dark Button created")
    
    def checkbox():
        print("Dark Checkbox created")
    
    def window():
        print("Dark Window created")


class LightThemeCreator(UICreator):
    def button():
        print("Light Button created")
    
    def checkbox():
        print("Light Checkbox created")
    
    def window():
        print("Light Window created")


class HighContrastThemeCreator(UICreator):
    def button():
        print("High Contrast Button created")
    
    def checkbox():
        print("High Contrast Checkbox created")
    
    def window():
        print("High Contrast Window created")




class UIFactory(ABC):
    @abstractmethod
    def create_ui(self):
        pass


class DarkThemeFactory(UIFactory):
    def create_ui(self):
        DarkThemeCreator.button()
        DarkThemeCreator.checkbox()
        DarkThemeCreator.window()


class LightThemeFactory(UIFactory):
    def create_ui(self):
        LightThemeCreator.button()
        LightThemeCreator.checkbox()
        LightThemeCreator.window()


class HighContrastThemeFactory(UIFactory):
    def create_ui(self):
        HighContrastThemeCreator.button()
        HighContrastThemeCreator.checkbox()
        HighContrastThemeCreator.window()




class Client:
    def __init__(self, factory: UIFactory):
        self.factory = factory.create_ui()
    



dark_ui = Client(DarkThemeFactory())
light_ui = Client(LightThemeFactory())
high_contrast_ui = Client(HighContrastThemeFactory())