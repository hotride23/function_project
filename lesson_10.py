# class Dog:
#     def __init__(self, height, weight, name, age):
#         self.name = name
#         self.height = height
#         self.weight = weight
#         self.age = age
#
#     def bark(self):
#         print('GAV GAV!')
#
#     def jump(self):
#         print('jump!')
#
#     def run(self):
#         print('run!')
#
#     def change_height(self, height):
#         self.height = height
#
#     def change_name(self, name):
#         self.name = name
#
#
# # dog_1 = Dog()
# # dog_1.bark()
# # dog_1.jump()
# # dog_1.run()
# dog_1 = Dog(100, 20, 'VASYA', 2)
# dog_2 = Dog(200, 50, 'George', 10)
# print(dog_1.height)
# print(dog_2.name)
# print(dog_1.age)
# print(dog_1.weight)
# print(dog_1.name)
# dog_1.bark()
# dog_1.jump()
# dog_1.run()
# dog_1 = Dog('Bob', 11, 12, 2015)
# print(dog_1.height)
# dog_1.change_height(15)
# print(dog_1.height)
# dog_1.change_name('kot')
# print(dog_1.name)
# class Dog:
#     def __init__(self, name, age, weight):
#         self.__name = name # private
#         self._age = age # protected
#         self.weight = weight # public
#
# dog = Dog('Bob', 8, 2.4)
# #print(dog.__name) # ERROR
# print(dog._Dog__name)
# print(dog._age)
# print(dog.weight)
# class Dog:
#     def __init__(self, name, age, weight, master):
#         self.__name = name # private
#         self._age = age # protected
#         self.weight = weight # public
#         self.__master = master
#     def get_master(self):
#         return self.__master
#
#
# dog = Dog('Bob', 8, 2.4, 'AUF')
# print(dog.get_master())
#
#
# class Dog:
#     def __init__(self, master):
#         self.__master = master
#     def get_master(self):
#         return self.__master
#     def set_master(self, master):
#         self.__master = master
#
#
# dog = Dog('Alex')
# print(dog.get_master())
# dog.set_master('Pavel')
# print(dog.get_master())
#
#
# class Object:
#     def __init__(self, address):
#         self.__address = address
#     def get_address(self):
#         return self.__address
#     def set_address(self, address):
#         self.__address = address
#
#
# wtf = Object('Minsk')
# print(wtf.get_address())
# wtf.set_address('Gomel')
# print(wtf.get_address())
#
#
# class Dog:
#     def __init__(self, master):
#         self.__master = master
#     @property
#     def master(self):
#         return self.__master
#     @master.setter
#     def master(self, master):
#         if len(master) < 5:
#             self.__master = master
#
#
# dog = Dog('Alex')
# dog.master = 'Moe'
# print(dog.master)
#
#
# class Dog:
#     def __init__(self, name, age, weight, height):
#         self.__name = name
#         self.__age = age
#         self.__weight = weight
#         self.__height = height
#
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self, age):
#         self.__age = age
#
#     @property
#     def weight(self):
#         return self.__weight
#     @weight.setter
#     def weight(self, weight):
#         self.__weight = weight
#
#     @property
#     def height(self):
#         return self.__height
#     @height.setter
#     def height(self, height):
#         self.__height = height
#
# dog = Dog('Alex', 2, 10, 50)
# print(dog.height)
# dog.name = 'Moet'
# print(dog.name)
#
#
# class Dog:
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
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
#     def sleep(self):
#         print('Zzz')
#
#     def bark(self):
#         print('AUF')
#
#
# class Cat:
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
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
#     def sleep(self):
#         print('Zzz')
#
#     def meow(self):
#         print('meow')
#
#
# class Parrot:
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
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
#     def sleep(self):
#         print('Zzz')
#
#     def fly(self):
#         print('ueeeeee')
#
#
# dog = Dog('Alex', 5, 100)
# print(dog.age)
# dog.birthday()
# print(dog.age)
#
#
# class Parent:
#     def print_world(self):
#         print('world')
#
#
# class Child(Parent):
#     def print_hello(self):
#         print('hello')
#
#
# class Pet:
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
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
#
# class Dog(Pet):
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#     def bark(self):
#         print('AUF')
#
#
# class Cat(Pet):
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#
#     def meow(self):
#         print('MEOW')
#
#
# class Parrot(Pet):
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#
#     def fly(self):
#         print('FLY!')
#
# cat = Cat('Alex', 10, 'M')
# dog = Dog('Fred', 2, 'F')
# parrot = Parrot('John', 30, 'M')
#
# cat.run()
# cat.meow()
# dog.jump()
# dog.bark()
# parrot.jump()
# parrot.fly()