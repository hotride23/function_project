def main():
    pass

# from datetime import datetime
# time = datetime.now()

# def my_decorator(func):
#     def do_some_staff():
#         print('hello world')
#         result = func()
#         return result
#     return do_some_staff
# def my_func():
#     pass
# my_new_func = my_decorator(my_func)
# my_new_func()


# def the_time(func):
#     def do_some_staff():
#         print(time)
#         result = func()
#         return result
#     return do_some_staff
#
#
# @the_time
# def my_func():
#     print('welcome')
#
# my_func()
#
#
# def moderate(func):
#     def do_even():
#         lister = func()
#         result = list(filter(lambda x: x % 2 == 0, lister))
#         print(result)
#         return func(), result
#     return do_even
#
#
# @moderate
# def my_func():
#     my_list = [i for i in range(10)]
#     return my_list
#
#
# my_func()
#
#
# my_file = open('test.txt')
# i = 1
# i_1 = 1
# i_2 = 1
# i_3 = 1
# i_4 = 1
# while True:
#     line = my_file.readline()
#     if not line:
#         break
#     elif i == 1:
#         print(line)
#     i += 1
# my_file.close()
#
#
# my_file = open('test.txt')
# while True:
#     line = my_file.readline()
#     if not line:
#         break
#     elif i_1 == 5:
#         print(line)
#     i_1 += 1
# my_file.close()
#
#
# my_file = open('test.txt')
# while True:
#     line = my_file.readline()
#     if not line:
#         break
#     elif i_2 < 6:
#         print(line)
#     i_2 += 1
# my_file.close()
#
#
# my_file = open('test.txt')
# while True:
#     line = my_file.readline()
#     if not line:
#         break
#     elif i_3 < 3:
#         print(line)
#     i_3 += 1
# my_file.close()
#
#
# my_file = open('test.txt')
# while True:
#     line = my_file.readline()
#     if not line:
#         break
#     print(line)
# my_file.close()
#
# my_file = open('test.txt')
# print(my_file.readlines())
# my_file.close()
#
#
# with open('test.txt') as my_file:
#     for line in my_file.readlines():
#         print(line)
#
#
# a = input('a: ')
# b = input('b: ')
# c = input('c: ')
# d = input('d: ')
# with open('test.txt', 'w') as my_file:
#     my_file.writelines(f'{a}\n{b}\n{c}\n{d}')
#
#
# with open('test.txt', 'w') as myfile:
#     ind = 1
#     while ind < 7:
#         c = input('str:  ')
#         ind += 1
#         myfile.write( c + '\n')
#
#
# with open('test.txt', 'a') as myfile:
#     ind = 0
#     while ind < 3:
#         c = input('str:  ')
#         ind += 1
#         myfile.write(c + '\n')
#
# #
# cache = []
# with open('test.txt', 'r') as test:
#     while True:
#         line = test.readline()
#
#         cache.append(str(line))
#         if not line:
#             break
#
#
# with open('test2.txt', 'w') as test2:
#     test2.writelines(i for i in cache)
#

if __name__ == '__main__':
    main()
