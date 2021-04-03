# Практическое задание 1
def new_file():
    status = True
    try:
        with open("new_file.txt", "w+", encoding="utf-8") as file:
            while status:
                user = input('Введите что надо записать в файл: ')
                my_list = [f"{user}\n"]
                file.writelines(my_list)
                user = input('Продолжить запись ? Y/N: ').upper()
                if user == "Y":
                    status = True
                else:
                    status = False
    except:
        print("Ошибка")


# Практическое задание 2
def open_file():
    try:
        with open(r"F:\2020\geekbrains\lesson5\text_2.txt", "r", encoding="utf-8") as file:
            for num, i in enumerate(file):
                print(f"Строка: {num + 1}, количество слов: {len(i.split())}")
    except:
        print("Error")


open_file()


# Практическое задание 3
def works():
    try:
        with open(r"F:\2020\geekbrains\lesson5\text_3.txt", "r", encoding="utf-8") as file:
            sum_works = 0
            for num, name in enumerate(file):
                if float(name.split()[1]) <= 20000:
                    name = name.replace('\n', '')
                    print(f"Фамилия: {name} руб")
                    sum_works += float(name.split()[1])
            print(f"Общая сумма зарплаты: {sum_works} руб")
    except:
        print('Error')


# Практическое задание 4

my_dict = {
    1: "Один",
    2: "Два",
    3: "Три",
    4: "Четыре"
}


def engl(my_dict):
    with open(r"F:\2020\geekbrains\lesson5\text_4.txt", "r", encoding='utf-8') as file, open("text4ru.txt", "a+",
                                                                                             encoding='utf-8') as fileru:
        for i in file.read().split('\n'):
            fileru.write(f"{my_dict[int(i.split('-')[1])]} -{i.split('-')[1]}\n")


# Практическое задание 5
def suma():
    with open('sum_file.txt', 'a', encoding='utf-8') as file:
        for i in [el for el in range(60, 80, 3)]:
            file.write(str(i) + '\n')

    with open('sum_file.txt', 'r', encoding='utf-8') as sum_file:
        ls = [int(el) for el in sum_file]
        print(sum(ls))


# Практическое задание 6
import re


def laba():
    my_dict = {}
    with open("text_6.txt", 'r', encoding='utf-8') as file:
        for thing in file.read().split('\n'):
            my_dict.update({thing.split(":")[0]: sum([int(el) for el in re.findall("\d+", thing)])})
    return my_dict


# Практическое задание 7
import json


def farm():
    firms = [{}, {}]
    with open("text_7.txt", "r", encoding="utf-8") as file:
        profit = 0
        for com in file.read().split("\n"):
            if int(com.split()[2]) > int(com.split()[3]):
                profit += int(com.split()[2]) - int(com.split()[3])
                firms[0][com.split()[0]] = int(com.split()[2]) - int(com.split()[3])
        firms[1]["average_profit"] = profit
    return json.dumps(firms)


# print(json.loads(farm()))

def priq():
    print("test")


priq()
