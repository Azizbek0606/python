# def reverse_number(n):
#     reversed_number = int(
#         str(abs(n))[::-1]
#     )
#     print(reversed_number)
#     return (
#         -reversed_number if n < 0 else reversed_number
#     )


# print(reverse_number(1234))
# print(reverse_number(-9876))
# print(reverse_number(1000))


# def find_duplicates(lst):
#     seen = set()
#     duplicates = set()
#     for num in lst:
#         if num in seen:
#             duplicates.add(num)
#         seen.add(num)
#     return sorted(duplicates)


# print(find_duplicates([1, 2, 3, 4, 5, 2, 3, 6, 7, 8, 1]))


# def longest_alpha_substring(s):
#     longest_substring = ""
#     current_substring = ""
#     for i in s:
#         if i.isalpha():
#             longest_substring += i
#         else:
#             if len(current_substring) < len(longest_substring):
#                 current_substring = longest_substring
#                 longest_substring = ""
#     return current_substring if len(current_substring) > len(longest_substring) else longest_substring

# print(longest_alpha_substring("abc1234xyz!!defg"))


# class Student:
#     def __init__(self, name, age, grades):
#         self.name = name
#         self.age = age
#         self.grades = grades
    
#     def get_average(self):
#         return sum(self.grades) / len(self.grades)


# s1 = Student("Ali", 20, [90, 85, 88])
# print(s1.get_average())


print([1,23] == not None)