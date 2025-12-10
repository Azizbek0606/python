# import copy

# class Person:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address

#     def clone(self):
#         return copy.deepcopy(self)

#     def __str__(self):
#         return f"{self.name} lives in {self.address}"
    

# class Address:
#     def __init__(self, city, country):
#         self.city = city
#         self.country = country
    
#     def __str__(self):
#         return f"{self.city}, {self.country}"


# sarvar = Person("Sarvar", Address("Tashkent", "O'zbekiston"))
# sevara = sarvar.clone()
# sevara.name = "Sevara"
# sevara.address.country = "UAE"
# print(sarvar)
# print(sevara)
