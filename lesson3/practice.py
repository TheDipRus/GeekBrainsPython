# def my_sum(arg_1, agr_2):
#     return arg_1 + agr_2

# print(my_sum(20, 30))
# print(my_sum('abra', 'kadabra'))


# def ext_func(var_1):
#     def int_func(var_2):
#         return var_1 + var_2

#     return int_func
# f_obj = ext_func(200)
# print(f_obj(300))


# def my_func():
#     pass
#
# print(my_func())


# def s_calc():
#     try:
#         r_val = float(input("Укажите радиус: "))
#         h_val = float(input("Укажите высоту: "))
#     except ValueError:
#         return
#     s_side = 2 * 3.14 * r_val * h_val
#     s_circle = 3.14 * r_val ** 2
#     s_full = s_side + 2 * s_circle
#     return s_side, s_full
#
#
# s_side_val, s_full_val = s_calc()
# print(f"Площадь боковой пов-ти - {s_side_val}; Полная площадь - {s_full_val}")


# def my_func(*args):
#     return args
# a, b, c, d = my_func(10, "text_1", 20, "text_2")
# print(a)
# print(b)
# print(c)
# print(d)


# my_finc = lambda *args: args
# print(my_finc(1, 2))


# obj_ = [20, 2, 5, 100]
# print(max(obj_))
# print(min(obj_))
# print(sum(obj_))

# print(list(range(-5, 6, 2)))

#
# for el in range(4, 20, 4):
#     res = el / 2
#     print(f"Результат деление {el} на 2: {int(res)}")

# def ext_func():
#     my_var = 0
#     def int_func():
#         nonlocal my_var
#         my_var += 1
#         return my_var
#     return int_func
#
#
# func_obj = ext_func()
# print(func_obj)
# print(func_obj())
# print(func_obj())
# print(func_obj())




























