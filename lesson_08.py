# list_a = [i for i in range(5)]
# list_b = [i ** 2 for i in [1, 2, 3]]
#
# print(list_a)
# print(list_b)
# #
# list = ["Hi", "Okay"]
# list_new = [i for i in list]
#
# names = ["Max", "Helen", "Alex", "Misha"]
# list_a = [name for name in names if "a" in name]
# print(list_a)
#
# list_dicts = [{'n': 1, 'y': 1993}, {'n': 2, 'y': 1995}, {'n': 3, 'y': 1998}, {'n': 4, 'y': 1959}, {'n': 5, 'y': 1994}]
# n = 1991
# list_b = [i for i in list_dicts for k, v in i.items() if v > n]
# print(list_b)
# from random import randint
# n = 5
# matrix = [[1 for j in range(n)] for i in range(n)]
# print(matrix)
#
# old_dict = {"aa" : 1, "b" : 2, "cccc" : 3}
# # new_dict = {key + str(len(key)) : value for key, value in old_dict.items()}
# # print(new_dict)
# #
# # old_dict = {"aa" : 1, "b" : 2, "cccc" : 3}
# # new_dict = {value : key for key, value in old_dict.items()}
# # print(new_dict)
# #
# def main():
#     #
#     # list_a = [1, 3, 5, 7, 54, 3, 5, 3, 7, 5, 3, 7, 2, 45, 54, 34, 3, 6, 3, 6, 8, 5, 3]
#     # n = 0
#     # diction_right_keys = {i: 1 for i in list_a}
#     # for k, v in diction_right_keys.items():
#     #     n = 0
#     #     for i in list_a:
#     #         if k == i:
#     #             n += 1
#     #     diction_right_keys[k] = n
#     # print(diction_right_keys)
#
# if __name__ == "__main__":
#     main()
#
# name = "Dima"
# func = lambda name: print(f"Hello, {name}")
# # func(name)
# list_names = ["Ira", "Dima", "Ivan"]
# hello_name = lambda name: [f'Hello {i}' for i in name]
# print(hello_name(list_names))
# a = [1, 2, 3, 4, 4, 4, 4, 4, 3, 1, 7, 8]
# # result = map(lambda x: x ** 2, a)
# # print(list(result))
# # a = [1, 2, 5, 10, 5]
# # result = map(lambda x: str(x), a)
# # print(list(result))
# result = list(filter(lambda x: x % 2 == 0, a))
# print(result)
# a = ['dima', 'alena', 'kot', 'fedor']
# result = list(filter(lambda x: 'k' in x, a))
# print(result)
# from functools import reduce
# # items = [1, 2, 3, 4, 5]
# # sum_all = reduce(lambda x, y: x + y, items)
# # print(sum_all)
# list_num = [1, 4, 9, 3]
# list_filter = list(filter(lambda x: x % 3 == 0, list_num))
# result = reduce(lambda x, y: x * y, list_filter)
# print(result)
