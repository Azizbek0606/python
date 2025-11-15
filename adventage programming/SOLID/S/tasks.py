# class UserAccountManager:
#     def validate_user(self):
#         pass
#     def send_welcome_message(self):
#         pass
    
    
# class UserDataManagement:
#     def create_user(self):
#         pass
#     def save_user(self):
#         pass


# class UserActivity:
#     def log_user_activity(self):
#         pass
#     def generate_user_report(self):
#         pass




# task 1
from abc import ABC , abstractmethod

class ShapeCalculator(ABC):
    @abstractmethod
    def areaCalculator(self):
        pass

class CircleAreaCalculator(ShapeCalculator):
    def areaCalculator(self):
        return super().areaCalculator()

class RectangArealeCalculator(ShapeCalculator):
    def areaCalculator(self):
        return super().areaCalculator()

class NewShapeAreaCalculator(ShapeCalculator):
    def areaCalculator(self):
        return super().areaCalculator()

class Calculate:
    def calculate(self, new_class):
        new_class.areaCalculator()







# task 2 

class Discount(ABC):
    @abstractmethod
    def discountCalculator(self):
        pass

class NewUser(Discount):
    def discountCalculator(self):
        return super().discountCalculator()

class VipUser(Discount):
    def discountCalculator(self):
        return super().discountCalculator()

class NewTypeUser(Discount):
    def discountCalculator(self):
        return super().discountCalculator()

class GetDiscount:
    def calculate(self, new_class):
        new_class.discountCalculator()





# task 3

class Notification(ABC):
    @abstractmethod
    def sendMessage(self):
        pass

class SmsMessage(Notification):
    def sendMessage(self):
        return super().sendMessage()

class PushMessage(Notification):
    def sendMessage(self):
        return super().sendMessage()
class NewTypeMessage(Notification):
    def sendMessage(self):
        return super().sendMessage()
    
class SendMessage:
    def send(self, new_class):
        new_class.sendMessage()







# task 4

class PaymentProcessor(ABC):
    @abstractmethod
    def payment(self):
        pass

class Humo(PaymentProcessor):
    def payment(self):
        return super().payment()

class UzCard(PaymentProcessor):
    def payment(self):
        return super().payment()

class Visa(PaymentProcessor):
    def payment(self):
        return super().payment()

class Payment:
    def pay(self, new_class):
        new_class.payment()






# task 5

class Reports(ABC):
    @abstractmethod
    def exportReport(self):
        pass

class PdfReport(Reports):
    def exportReport(self):
        return super().exportReport()

class DocReport(Reports):
    def exportReport(self):
        return super().exportReport()

class TxtReport(Reports):
    def exportReport(self):
        return super().exportReport()
      
class ExportReport:
    def export(self, new_class):
        new_class.exportReport()

# task 6

class Tax(ABC):
    @abstractmethod
    def taxcalculator(self):
        pass

class UsaTax(Reports):
    def taxcalculator(self):
        return super().taxcalculator()

class UkTax(Reports):
    def taxcalculator(self):
        return super().taxcalculator()

class UzTax(Reports):
    def taxcalculator(self):
        return super().taxcalculator()
      
class CalculateTax:
    def calculate(self, new_class):
        new_class.taxcalculator()