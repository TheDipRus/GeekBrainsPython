# Практическое задание 1

from sys import argv
work_time, money_hour, prize = argv[1:]
print(f"Зарплата за {work_time} часов: {int(work_time) * int(money_hour)} руб\nПремия: {int(prize)} руб ")


# Практическое задание 2

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(new_list)

ll = []
for el in range(1, len(my_list)):
    if my_list[el] > my_list[el - 1]:
        ll.append(my_list[el])
print(ll)



# Практическое задание 3

my_list = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
print(my_list)



# Практическое задание 4

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [el for num, el in enumerate(my_list) if my_list.count(my_list[num]) == 1]
print(new_list)



# Практическое задание 5
from functools import reduce
my_list = [el for el in range(100, 1001) if el % 2 == 0]

print(reduce(lambda a, b: a * b, my_list))

print(reduce(lambda a, b: a * b, [el for el in range(100, 1001, 2)]))

# Практическое задание 6
import itertools


def gen_int(a):
    my_list = []
    for i in itertools.count(a):
        if i > 10:
            break
        else:
            my_list.append(i)
    return my_list, a


def cyc(ls, num):
    c = 0
    for i in itertools.cycle(ls):
        if c > num:
            break
        print(i)
        c += 1


cyc(gen_int(5)[0], gen_int(5)[1])

# Практическое задание 7
import math


def fact():
    yield [el for el in range(11)]


for i in fact():
    print(math.factorial(i))