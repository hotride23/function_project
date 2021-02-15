# class A:
#     def __init__(self):
#         self.weight = 0
#         self.height = 0
#
#     def change_weight(self, weight):
#         self.weight = weight
#
#     def change_height(self, height):
#         self.height = height
#
#
# class Parrot(A):
#     def change_weight(self, weight):
#         if weight is int or float:
#             self.weight = weight
#         else:
#             self.weight += 0.05
#
# x = Parrot()
# x.change_weight(5)
# print(x.weight)
# x.change_weight('a')
# print(x.weight)
#
#
# class A:
#     def do_something(self):
#         print('aa')
#
#
# class B(A):
#     def do_something(self):
#         super().do_something()
#         print('bb')
#
#
# x = B()
# print(x.do_something())
#
#
# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#     def jump(self, jump):
#         print(f'Jump {jump} meters')
#
#
# class Dog(Pet):
#     def jump(self, jump):
#         if jump > 0.5:
#             print('Dogs cannot jump so high')
#         else:
#             super().jump(jump)
#
#
# class Cat(Pet):
#     def jump(self, jump):
#         if jump > 2:
#             print('Cats cannot jump so high')
#         else:
#             super().jump(jump)
#
#
# class Parrot(Pet):
#     def jump(self, jump):
#         if jump > 0.05:
#             print('Dogs cannot jump so high')
#         else:
#             super().jump(jump)
#
#
# x = Dog('alex', 2)
# x.jump(0.3)
# x.jump(11)
#
#
# class A:
#     def __init__(self, a):
#         self.a = a
#
#
# class B(A):
#     def __init__(self, a, b):
#         super().__init__(a)
#         self.b = b
#
# x = B(1, 10)
# print(x.a)

# class Dog(Pet):
#     def jump(self, jump):
#         if jump > 0.5:
#             print('Dogs cannot jump so high')
#         else:
#             super().jump(jump)
#
#
# class Cat(Pet):
#     def jump(self, jump):
#         if jump > 2:
#             print('Cats cannot jump so high')
#         else:
#             super().jump(jump)
#
#
# class Parrot(Pet):
#     def jump(self, jump):
#         if jump > 0.05:
#             print('Dogs cannot jump so high')
#         else:
#             super().jump(jump)
#
#
# class Pet:
#     def __init__(self):
#         self.name = None
#         self.age = None
#         self.master = None
#
#     def run(self):
#         print('run!')
#
#     def jump(self):
#         print('jump!')
#
#     def birthday(self):
#         self.age += 1
#
#     def voice(self):
#         pass
#
#
# class Dog(Pet):
#     def voice(self):
#         print('AUF')
#
#
# class Cat(Pet):
#     def voice(self):
#         print('MEOW')
#
#
# class Parrot(Pet):
#     def fly(self):
#         print('FLY!')
#
#
# cat = Cat()
# dog = Dog()
# parrot = Parrot()
#
#
# def my_func(*args):
#     for i in args:
#         i.voice()
#
#
# my_func(cat, dog, parrot)
# print(dir(cat))
#
#
# class Car:
#     last_model = None
#
#     def __init__(self, model):
#         self.model = model
#         Car.last_model = model
#
#
# car1 = Car('A')
# print(Car.last_model)
# car2 = Car('B')
# print(Car.last_model)
# print(car1.last_model)
#
#
# class Pet:
#     __counter = 0
#
#     def __init__(self):
#         self.name = None
#         self.age = None
#         self.master = None
#
#
#
#     @property
#     def counter(self):
#         return self.__counter
#
#     @counter.setter
#     def counter(self, counter):
#         self.__counter = counter
#
#     def run(self):
#         print('run!')
#
#     def jump(self):
#         print('jump!')
#
#     def birthday(self):
#         self.age += 1
#
#     def voice(self):
#         pass
#
#
# class Dog(Pet):
#
#     def voice(self):
#         print('AUF')
#
#
# class Cat(Pet):
#     def voice(self):
#         print('MEOW')
#
#
# class Parrot(Pet):
#     def fly(self):
#         print('FLY!')
#
#
# cat = Cat()
# dog = Dog()
# parrot = Parrot()
# x = Dog()
# z = Cat()
#
# print(dog.counter)
# class Car:
#     __last_model = None
#
#     def __init__(self, model):
#         self.__last_model = model
#         Car.__last_model = model
#
#     @classmethod
#     def get_last_model(cls):
#         return cls.__last_model
#
#
# car1 = Car('A')
# print(Car.get_last_model())
# print(car1.get_last_model())
#
#
# class Car:
#     counter = 0
#     __last_model = None
#
#     def __init__(self, model):
#         self.__last_model = model
#         Car.counter += 1
#
#     @classmethod
#     def get_counter(cls):
#         return cls.counter
#
#
# car1 = Car('A')
# print(Car.get_counter())
