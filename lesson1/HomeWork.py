# Практическое задание 1

# name = input('Введите имя: ')
# age = int(input('Введите возраст: '))
# print(f'Меня зовут {name}, мне {age} лет')



# Практическое задание 2

# time = int(input('Введите время в секундах: '))
# seconds = time % 60
# time = time - seconds
# hours = time / 3600
# time = time - (hours * 3600)
# mins = time / 60
# print(f'{int(hours)}:{int(mins)}:{int(seconds)}')



# Практическое задание 3

# n = input('Введите число: ')
# sum1 = n
# sum2 = n + n
# sum3 = n + n + n
# print(f'{sum1} + {sum2} + {sum3} = {int(sum1) + int(sum2) + int(sum3)}')



# Практическое задание 4

# num = int(input('Введите число: '))
# while True:
#     num1 = num % 10     # Последнее число
#     num2 = num // 10    # Первое число
#     if num1 > num2:
#         print(num1)
#         break
#     elif num1 == num2:
#         print('Они ровны')
#         break
#     else:
#         print(num2)
#         break



# Практическое задание 5

# costs = int(input("Введите расходы фирмы: "))
# income = int(input("Введите доходы фирмы: "))
# profit = income - costs
# if income > costs:
#     print(f"В данный момет компания имеет прибыль в размере: {profit} руб.")
#     staff = int(input("Введите количество сотрудников: "))
#     print(f"Количество сотрудников: {staff}, прибыль на 1 сотрудника {profit / staff:.0f} руб.")
# else:
#     print(f"Убыток составил: {profit} руб.")



# Практическое задание 6


# day1 = int(input('Введите количество километров в 1 день: '))
# day2 = int(input('Введите общие количество километров: '))
# i = 0
# while day1 < day2:
#     procent = day1 / 100 * 10
#     i += 1
#     day1 += procent
#     print(f"{i}-й день: {day1:.2f} ")


