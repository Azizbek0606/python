# from abc import ABC, abstractmethod

# class CreditCardPayment(ABC):
#     @abstractmethod
#     def pay_with_credit_card(self):
#         pass

# class PayPalPayment(ABC):
#     @abstractmethod
#     def pay_with_paypal(self):
#         pass

# class CryptoPayment(ABC):
#     @abstractmethod
#     def pay_with_crypto(self):
#         pass

# class PayPal(PayPalPayment):
#     def pay_with_paypal(self):
#         print("PayPal orqali to'lov amalga oshirildi")

# class CreditCard(CreditCardPayment):
#     def pay_with_credit_card(self):
#         print("Kredit karta orqali to'lov")

# class Bitcoin(CryptoPayment):
#     def pay_with_crypto(self):
#         print("Bitcoin orqali to'lov")


# file exporter

# class FileExpoeter(ABC):
#     @abstractmethod
#     def export_csv(self):
#         pass

#     @abstractmethod
#     def export_pdf(self):
#         pass

#     @abstractmethod
#     def export_excel(self):
#         pass

# class ExportPdfFile(FileExpoeter):
#     def export_csv(self):
#         pass

#     def export_excel(self):
#         pass
    
#     def export_pdf(self):
#         print("ota classdan faqat ushbu method kerak!")

# file exporter true version

# class CsvExporter(ABC):
#     @abstractmethod
#     def export_csv(self):
#         print("send csv file")

# class PdfExporter(ABC):
#     @abstractmethod
#     def export_pdf(self):
#         print("send pdf file")

# class ExcelExporter(ABC):
#     @abstractmethod
#     def export_excel(self):
#         print("send excel file")


# class ExportCsvFile(CsvExporter):
#     def export_csv(self):
#         return super().export_csv()


# class ExportExcelFile(ExcelExporter):
#     def export_excel(self):
#         return super().export_excel()
    

# class ExportPdfFile(PdfExporter):
#     def export_pdf(self):
#         return super().export_pdf()




# Main Task
# class PaymentGateway():
#     def charge(self, amount: float) -> bool:
#         print(amount)
#         return True


# class StripeGateway(PaymentGateway):
#     def charge(self, amount):
#         return super().charge(amount)
    

# class PayPalGateway(PaymentGateway):
#     def charge(self, amount):
#         return super().charge(amount)
    

# class CryptoGateway(PaymentGateway):
#     def charge(self):
#         raise NotImplemented

# stripe = StripeGateway()
# paypal = PayPalGateway()
# crypto = CryptoGateway()


# def process_payment(gateway: PaymentGateway, amount:float):
#     gateway.charge(amount)

# process_payment(stripe, 100.02)  
# process_payment(paypal, 50.78)   
# process_payment(crypto, 100.53)            


# main task true version

# class PaymentGateway():
#     def charge(self, amount: float) -> bool:
#         print(amount)
#         return True
    

# class CryptoMainGateway():
#     def crypto_charge(self, amount:float) -> bool:
#         print("Cripto Charge")
#         return True


# class StripeGateway(PaymentGateway):
#     def charge(self, amount):
#         return super().charge(amount)
    

# class PayPalGateway(PaymentGateway):
#     def charge(self, amount):
#         return super().charge(amount)

# class CryptoGateway(CryptoMainGateway):
#     def crypto_charge(self, amount):
#         return super().crypto_charge(amount)
    
# def process_payment(gateway: PaymentGateway, amount:float):
#     gateway.charge(amount)

# def progress_crypto_payment(gateway: CryptoMainGateway, amount : float):
#     gateway.crypto_charge(amount)

# stripe = StripeGateway()
# paypal = PayPalGateway()
# crypto = CryptoGateway()
# process_payment(stripe, 100.02)  
# process_payment(paypal, 50.78)   
# process_payment(crypto, 100.53)   


# online book booking system

class Book:
    def __init__(self, title, price, has_discount):
        self.title = title
        self.price = price
        self.has_discount = has_discount
    
class Order:
    list_item = []
    def __init__(self, item_list, customer, total_price, is_completed, discount_applied):
        for i in item_list:
            self.list_item.append(i)
        self.customer = customer
        self.total_price = total_price
        self.is_complated = is_completed
        self.discount_applied = discount_applied
    
    def add_book(self, customer, total_price, is_complated, discount_applied):
        order = []
        order.append(customer)
        order.append(total_price)
        order.append(is_complated)
        order.append(discount_applied)
        self.list_item(order)

    def calculate_total(self):
        