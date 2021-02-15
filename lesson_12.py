# class Car:
#     __last_model = None
#
#     def __init__(self, model):
#         self.model = model
#         Car.__last_model = model
#
#     @staticmethod
#     def is_model_ok(model):
#         return len(model) > 3
#
#
# print(Car.is_model_ok('abc'))
# class Car:
#     __last_model = None
#
#     def __init__(self, model):
#         self.model = model
#         Car.__last_model = model
#
#     @staticmethod
#     def reverse(str):
#         return str[::-1]
#
# print(Car.reverse('abcd'))
#
#
# class A:
#     def hi(self):
#         print('a')
#
# class B(A):
#     def hi(self):
#         print('b')
#
# class C(A):
#     def hi(self):
#         print('c')
#
# class D(B, A):
#     pass
#
# d = D()
# d.hi()
#
#
# class Pet:
#     def __init__(self):
#         pass
#
#     def voice(self):
#         pass
#
#
# class Horse(Pet):
#     def voice(self):
#         print('IGAGA')
#
#
# class Donkey(Pet):
#     def voice(self):
#         print('IGOGO')
#
#
# class Mule(Donkey, Horse):
#     pass
#
#
# horse = Horse()
# horse.voice()
# donkey = Donkey()
# donkey.voice()
# mule = Mule()
# mule.voice()
#
#
# a = int(input('a: '))
# b = int(input('b: '))
# try:
#     result = a / b
# except ZeroDivisionError as err:
#     print(f'b is zero - {err}!')
# except Exception as err:
#     print(f'Something wrong - {err}!')
# else:
#     print('No error')
# finally:
#     print('Always work')
#
#
# class MyException(Exception):
#     def __init__(self, message = 'AAA!!'):
#         super().__init__(message)
#
# raise MyException('sad')
#
#
# class Book:
#     def __init__(self, pages, year, author, price):
#         try:
#             self.pages = int(pages)
#         except ValueError as err:
#             print('Необходимо ввести числа в количестве страниц!!!')
#         try:
#             self.year = int(year)
#         except ValueError as err:
#             print('Необходимо ввести числа в году книги!!!')
#         try:
#             self.author = str(author)
#         except TypeError as err:
#             print('Необходимо ввести имя автора книги!!!')
#         try:
#             self.price = int(price)
#             if price < 0:
#                 raise Exception('You give negative!', price)
#         except ValueError as err:
#             print('Необходимо ввести числа в цене книги!!!')
#
#
# abc = Book(1, 2, 'a', -1)
# print(abc.pages)
# print(abc.author)
# print(abc.price)
# print(abc.year)
# bca = Book(1, 2, 'a', 5)
# print(bca.pages)
# print(bca.author)
# print(bca.price)
# print(bca.year)
#
#
# class MyErr(Exception):
#     def __init__(self, mess='Zero cost'):
#         super().__init__(mess)
#
#
# class Book:
#     def __init__(self, pages, year, author, cost):
#         try:
#             self.pages = pages
#             self.year = year
#             self.author = author
#             self.cost = cost
#             if type(pages) != int:
#                 raise TypeError('Pages is not int')
#             if type(year) != int:
#                 raise TypeError('Year is not int')
#             if type(author) != str:
#                 raise TypeError('Author is not str')
#             if type(cost) != int:
#                 raise TypeError('Cost is not int')
#             if year > 2021:
#                 raise ValueError('Error year')
#
#             if cost == 0:
#                 raise MyErr
#
#         except TypeError as te:
#             print(te)
#
#         except ValueError as ve:
#             print(ve)
#
#         except MyErr as err:
#             print(f'cost is not valid - {err}')
#         else:
#             print('Data is correct')
#
#
# a = Book('str', 2022, 'Author', 10)
# b = Book(12, 'str', 'author', 10)
# c = Book(12, 2000, 45, 10)
# d = Book(12, 200, 'author', [])
# e = Book(12, 3000, 'author', 10)
# f = Book(12, 2000, 'author', 0)
# from abc import ABC, abstractmethod
#
# class A(ABC):
#     @abstractmethod
#     def do_smth(self):
#         print('im a parent')
#
# class B(A):
#     def do_smth(self):
#         print('im a child')
#
# # a = A()
# # b = B()
# A.do_smth('a')
