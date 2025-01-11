# def ichki_generator():
#     yield 1
#     yield 2
#     yield 2


# def tashqi_generator():
#     yield "Boshlanish"
#     yield from ichki_generator()  # ichki generatordan ma'lumotlarni olamiz
#     yield "Tugash"


# for qiymat in tashqi_generator():
#     print(qiymat)


# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b


# gen = fibonacci()

# for _ in range(10):
#     print(next(gen))


# def sonlar():
#     for i in range(1, 101):
#         yield i


# def juft_sonlar(gen):
#     for son in gen:
#         if son % 2 == 0:
#             yield son


# def kvadrat(gen):
#     for son in gen:
#         yield son**2


# pipeline = kvadrat(juft_sonlar(sonlar()))
# for natija in pipeline:
#     print(natija)


# royxat = [1, 2, 3, 4, 5]

# iterator = iter(royxat)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


# import random


# def tasodifiy_son():
#     return random.randint(1, 10)


# iterator = iter(tasodifiy_son, 7)
# for son in iterator:
#     print(son)


# arr = [1,2,3]

# iterator = iter(arr)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# def generator_func():
#     yield 1
#     yield 2
#     yield 3

# gen = generator_func()

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


# def genorator_func():
#     for i in range(1, 4):
#         yield i
#     print("Generator")

# gen = genorator_func()

# print(next(gen))
# print(next(gen))
# print(next(gen))


# class CustomIterator:
#     def __init__(self, limit):
#         self.limit = limit
#         self.current = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current < self.limit:
#             self.current += 1
#             return self.current
#         else:
#             raise StopIteration


# # Iterator yaratish
# my_iter = CustomIterator(3)
# for value in my_iter:
#     print(value)


# def example():
#     yield 1
#     yield 2
#     yield 3
#     yield 4

# print(next(example()))
# print(next(example()))
# print(next(example()))
# print(next(example()))

# arr = [1, 2, 3, 4]
# x = iter(arr)
# print(next(x))