# from abc import ABC, abstractmethod
#
# class Weapon(ABC):
#     @abstractmethod
#     def shoot(self):
#         pass
#
#
# class AK47(Weapon):
#     def shoot(self):
#         return "AK47"
#
# class MK14(Weapon):
#     def shoot(self):
#         return "MK14"
#
# class AWP(Weapon):
#     def shoot(self):
#         return "AWP"
#
# class KAR45(Weapon):
#     def shoot(self):
#         return "KAR45"
#
# class Player(ABC):
#     def __init__(self, gun:Weapon):
#         self.gun = gun
#
#     @abstractmethod
#     def fight(self):
#         pass
#
#
# class WhitePlayer(Player):
#     def fight(self):
#         return "White Player Shooting with " + self.gun.shoot()
#
# class BlackPlayer(Player):
#     def fight(self):
#         return "Black Player Shooting with " + self.gun.shoot()
#
#
# # Test
# ak47 = AK47()
# mk14 = MK14()
# awp = AWP()
# kar45 = KAR45()
# white_player = WhitePlayer(ak47)
# black_player = BlackPlayer(mk14)
# print(white_player.fight())
# print(black_player.fight())
# white_player = WhitePlayer(awp)
# black_player = BlackPlayer(kar45)
# print(white_player.fight())
# print(black_player.fight())
from enum import Enum


# class PayPall:
#     def func_pay(self):
#         return "PayPall"
#
# class MasterCard:
#     def func_mc(self):
#         return "MasterCard"
#
# class USDPayPall(PayPall):
#     def pay(self):
#         return "USD: " + self.func_pay()
#
#
# class EuroPayPall(PayPall):
#     def pay(self):
#         return "Euro: " + self.func_mc()
#
#
# class USDMasterCard(MasterCard):
#     def pay(self):
#         return "USD: " + self.func_pay()
#
#
# class EuroMasterCard(MasterCard):
#     def pay(self):
#         return "Euro: " + self.func_mc()
#
from abc import ABC


class Valute(ABC):
    def pay(self):
        pass

class USD(Valute):
    def pay(self):
        return "USD"

class Euro(Valute):
    def pay(self):
        return "Euro"


class PaymentMethod(ABC):
    def __init__(self, valute: Valute):
        self.valute = valute

    def func_pay(self):
        pass

class PayPall(PaymentMethod):
    def func_pay(self):
        return "PayPall: " + self.valute.pay()

class MasterCard(PaymentMethod):
    def func_pay(self):
        return "MasterCard: " + self.valute.pay()

# usd = USD()
# euro = Euro()
# payment = PayPall(usd)
# print(payment.func_pay())
# payment = PayPall(euro)
# print(payment.func_pay())