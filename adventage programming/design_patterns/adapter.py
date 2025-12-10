# from abc import ABC, abstractmethod

# # 1. Bizda mavjud bo'lgan, lekin interfeysi boshqacha bo'lgan klasslar
# class EmailSender:
#     def send_email(self, message):
#         print(f"Email orqali yuborildi: {message}")

# class SMSSender:
#     def send_sms(self, message):
#         print(f"SMS orqali yuborildi: {message}")

# class TelegramSender:
#     def push(self, message):
#         print(f"Telegram orqali yuborildi: {message}")

# # 2. Umumiy interfeys (Target interface)
# class INotifier(ABC):
#     @abstractmethod
#     def send_message(self, message: str):
#         pass

# # 3. Adapterlar — eski klasslarni yangi interfeysga moslashtiramiz
# class EmailAdapter(INotifier):
#     def __init__(self, email_sender: EmailSender):
#         self.email_sender = email_sender
    
#     def send_message(self, message: str):
#         self.email_sender.send_email(message)

# class SMSAdapter(INotifier):
#     def __init__(self, sms_sender: SMSSender):
#         self.sms_sender = sms_sender
    
#     def send_message(self, message: str):
#         self.sms_sender.send_sms(message)

# class TelegramAdapter(INotifier):
#     def __init__(self, telegram_sender: TelegramSender):
#         self.telegram_sender = telegram_sender
    
#     def send_message(self, message: str):
#         self.telegram_sender.push(message)

# # 4. Client — faqat INotifier bilan ishlaydi
# class NotificationClient:
#     def __init__(self, notifier: INotifier):
#         self.notifier = notifier
    
#     def notify(self, message: str):
#         self.notifier.send_message(message)

# # ======================= Ishlatish =======================
# email_sender = EmailSender()
# sms_sender = SMSSender()
# telegram_sender = TelegramSender()

# # Adapterlar orqali moslashtiramiz
# email_notifier = EmailAdapter(email_sender)
# sms_notifier = SMSAdapter(sms_sender)
# telegram_notifier = TelegramAdapter(telegram_sender)
# # Client faqat bitta interfeys bilan ishlay oladi
# client = NotificationClient(email_notifier)
# client.notify("Salom, bu test xabar!")  # Email orqali yuborildi

# client = NotificationClient(sms_notifier)
# client.notify("Kod: 123456")  # SMS orqali yuborildi

# client = NotificationClient(telegram_notifier)
# client.notify("Yangi buyurtma!")  # Telegram orqali yuborildi





# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.left = left
#         self.right = right
#         self.value = value

# a8 = Node(8)
# a7 = Node(7)
# a6 = Node(6)
# a5 = Node(5, None, a8) 
# a4 = Node(4)
# a3 = Node(3, a6, a7)    
# a2 = Node(2, a4, a5)   
# a1 = Node(1, a2, a3)

# visited = []

# def preorder_traversal(root): 
#     if root is None:       
#         return
#     visited.append(root.value)
#     preorder_traversal(root.left)
#     preorder_traversal(root.right)


# preorder_traversal(a1)
# print(visited)