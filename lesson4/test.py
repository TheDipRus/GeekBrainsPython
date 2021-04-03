# my_list = [1, 2, 3, 4, 5, 6]
#
# new_1 = [el ** 3 for el in my_list]
# new_2 = (el ** 3 for el in my_list)



# from random import randint, randrange, random
# print(randint(1000, 9999))
# print(randrange(8, 88))
# print(random() * 10)


# def gen():
#     for el in {1, 2, 3, 4}:
#         yield el
#
#
# print(list(gen()))
# # for i in gen():
# #     print(i)


# from functools import reduce
# def my_func(prev_el, el):
#     return prev_el + el
# print(reduce(my_func, [1,2,3,4,5,6]))

# from itertools import count
#
# for el in count(0.1, 0.001):
#     print(el)
#####################################################################
# import time
# import random
# print(time.time())
# print(random.random())


# from time import time
# from random import random
# print(time())
# print(random())


# from sys import argv
# script_name, first_param, second_param, third_param = argv
# print("Имя скрипта: ", script_name)
# print("Параметр 1: ", first_param)
# print("Параметр 2: ", second_param)
# print("Параметр 3: ", third_param)


# my_list = [2, 4, 6]
# new_list = [el + 10 for el in my_list]
# print(f"Исходный список: ", my_list)
# print(f"Измененный список: ", new_list)


# import random
# print(random.randint(0, 10))
# from random import randint
# # from random import randrange
# from random import random
# print(int(random() * 10000))
# # print(randint(-100, -78))



# from functools import reduce
# def my_func(prev_el, el):
#     # prev_el - предыдущий элемент
#     # el - текущий элемент
#     return prev_el + el
# a = [20, 20, 30, 60]
# print(reduce(my_func, a))


# from itertools import count
#
# for el in count(8):
#     if el > 100:
#         break
#     else:
#         print(el)


progr_lang = ["python", "java", "perl", "javascript"]
