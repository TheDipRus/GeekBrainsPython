# python 3.9

import random


with open("city.txt", 'r', encoding='utf-8') as open_file:
    city_computer_list = [el.replace(' ', '') for el in open_file.read().split()]


computer_work = random.randint(0, len(city_computer_list))
it_was_city_computer = []
it_was_city_user = []


def user_words():
    """
    Запрос города от пользователя.
    Оброботка кривых запросов.
    """
    while True:
        user = input("Введите город: ").title()
        if user in city_computer_list:
            if user in it_was_city_computer:
                print('Города не должны повторяться')
                continue
            elif user in it_was_city_user:
                print('Города не должны повторяться')
                continue
            elif user.isalpha() and len(user) >= 3:
                it_was_city_user.append(user)
                return user
            else:
                print("Название должно содержать только буквы")
        else:
            print('Я сомневаюсь что это город, попробуй еще раз')


def logics():
    while True:
        # Последняя буква пользователя
        user_word = user_words()
        if user_word[-1] == "ь" or user_word[-1] == "ъ" or user_word[-1] == "й" or user_word[-1] == "ы":
            last_letter = user_word[-2]
        else:
            last_letter = user_word[-1]

        # Поиск городов компьютера, по последней буквы
        for city in city_computer_list:
            if city[0].lower() == last_letter:
                it_was_city_computer.append(city)
                computer_words = city_computer_list.pop(city_computer_list.index(city))
                print(computer_words)

        else:
            print(f'Я больше незнаю городов на букву: {last_letter.upper()}\nВы выиграли !')

        # Проверка правильности ввода города пользователя




print(logics())













# def main():
#     while True:
#         if user_words()[0] == computer_input()[-1]:
#             computer_input()
#         else:
#             print(f"Город должен называться на букву {computer_input()[-1]}")



















# while True:
#
#     user_word = input("Введите город: ").lower()
#
#
#     if user_word[-1] == "ь" or user_word[-1] == "ъ" or user_word[-1] == "й" or user_word[-1] == "ы":
#         last_letter = user_word[-2]
#     else:
#         last_letter = user_word[-1]
#
#     # Поиск городов компьютера
#     for city in city_computer_list:
#         if city[0].lower() == last_letter:
#             it_was_city.append(city)
#             print(city_computer_list.pop(city_computer_list.index(city)))
#             break
#     else:
#         print(f'Я больше незнаю городов на букву: {last_letter.upper()}\nВы выиграли !')
