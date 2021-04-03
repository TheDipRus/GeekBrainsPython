# Практическое задание 1
def division():
    """Зашита от деления на 0"""
    num1 = float(input('Введите 1 число: '))
    num2 = float(input('Введите 2 число: '))
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Деление на 0"


# Практическое задание 2
def about(name, surname, year, city, email, phone):
    """User data"""
    print(f"{name} {surname} {year} {city} {email} {phone}")


# Практическое задание 3
def my_func(arg_1, arg_2, arg_3):
    """возвращает сумму наибольших двух аргументов"""
    my_list = [arg_1, arg_2, arg_3]
    my_list.remove(min(my_list))
    return sum(my_list)


def my_func4(a, b, c):
    list_s = sorted((a, b, c))
    return sum(list_s[1:])


# Практическое задание 4  ??????????????????????
def my_func2(x, y):
    return x ** y


def my_func3(x, y):
    my_list = []
    for _ in range(1, y + 1):
        my_list.append(x)
    res = my_list[0]
    for i in range(len(my_list)):
        res += my_list[i] * res
    return res


# Практическое задание 5
def us_func():
    status = True
    res_sum = 0
    while status:
        num = input('Введите числа через пробел:').lower()
        my_list = num.split()
        l_sum = 0
        for i in my_list:
            if i == 'q':
                status = False
            else:
                l_sum += int(i)
        res_sum += l_sum
        print(f"Сумма чисел: {l_sum}\nОбщая сумма: {res_sum}")


# Практическое задание 6

def int_func(word):
    return word.title()


def int_func2(word):
    return ' '.join(word.split()).title()




