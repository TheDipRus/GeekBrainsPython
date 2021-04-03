# Практическое задание 1
# my_list = ["str", 1, 2.53, True]
# for i in my_list:
#     print(type(i))

# Нормальное решение
# my_list = ["str", 1, 2.53, True]
# for i, item in enumerate(my_list, 1):
#     print(f"{i} {item} - {type(item)}")

# Практическое задание 2
# my_list = list(input('Введите цифры без пробела - '))
# for i in range(1, len(my_list), 2):
#     my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
# print(my_list)

# my_list = list(input('Введите цифры без пробела - '))
# for i in range(1, len(my_list), 2):
#     my_list.insert(i - 1, my_list.pop(i)
# print(my_list)


# Практическое задание 3
# seasons = {
#     "Зима": [12, 1, 2],
#     "Весна": [3, 4, 5],
#     "Лето": [6, 7, 8],
#     "Осень": [9, 10, 11]
# }
#
# while True:
#     user = int(input("Введите месяц: "))
#     if user >= 1 and user <= 12:
#         for i in seasons.items():
#             if i[1].count(user) == 1:
#                 print(i[0])
#         break
#     else:
#         print("Введите месяц от 1 до 12")


# Практическое задание 4
# user = input('Введите слова через пробел: ')
# my_list = user.split()
# for word in my_list:
#     print(word[:10])

# user = input('Введите слова через пробел: ').split()
# for i, word in enumerate(user, 1):
#     print(f"{i} {word[:10]}")


# Практическое задание 5
# user = float(input("Введите оценку: "))
# rating = [7, 5, 3, 3, 2]
#
# for i in range(len(rating)):
#     if rating[i] >= user and rating[i + 1] <= user:
#         rating.insert(i + 1, user)
#         break
#     if rating.count(user) == 0:
#         if rating[0] > user:
#             rating.insert(len(rating), user)
#             break
#         else:
#             rating.insert(0, user)
#             break
#
# print(rating)


# rating = [7, 5, 3, 3, 2]
# user = float(input("Введите оценку: "))
# i = 0
# for n in rating:
#     if user <= n:
#         i += 1
# rating.insert(i, user)
# print(rating)

# Практическое задание 6

# products_id = []
#
# prod_id = 0
# status = True
# while status:
#     # Меню
#     print('*' * 36)
#     print('* Добро пожаловать в меню "Товары" *')
#     print('*' * 36)
#     print(f'* {" " * 6}1). Добавить товар  {" " * 6} *')
#     print(f'* {" " * 6}2). Удалить товар  {" " * 7} *')
#     print(f'* {" " * 6}3). Аналитика товара  {" " * 4} *')
#     print(f'* {" " * 6}4). Выход  {" " * 15} *')
#     print(f"{'*' * 36}")
#     user_add = int(input('Введите цифру: '))
#     # Добавление Товара
#     if user_add == 1:
#         print('\nДобавление товаров')
#         name = input("Введите название торвара: ")
#         price = input("Введите цену торвара: ")
#         quantity = input("Введите количество торвара: ")
#         units = "шт"
#         products_name = {"название": name, "цена": price, "количество": quantity, "ед": units}
#         prod_id += 1
#         products_id.append((prod_id, products_name))
#         print('\n-> Товар успешно добавлен\n')
#         print(products_id, sep='\n')
#         continue
#     # Удаление товара
#
#
#     # Выход из программы
#     if user_add == 4:
#         status = False


# products_id = []
#
# prod_id = 0
# status = True
# while status:
#     print('Добавление товаров')
#     name = input("Введите название торвара: ")
#     price = input("Введите цену торвара: ")
#     quantity = input("Введите количество торвара: ")
#     units = "шт"
#     products_name = {"название": name, "цена": price, "количество": quantity, "ед": units}
#     prod_id += 1
#     products_id.append((prod_id, products_name))


goods = []
features = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analitics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0
while True:
    if input("Для выхода нажмите Q, для подолжения Enter: ").upper() == 'Q':
        break
    num += 1
    for f in features.keys():
        pro = input(f"Введите значение свойства {f}: ")
        features[f] = int(pro) if f == 'цена' or f == 'количество' else pro
        analitics[f].append(features[f])
    goods.append((num, features))
    print(f"\nСтруктура товаров\n{goods}")
    print(f"\n Текущая аналитика: \n {'*' * 30}")
    for k, v in analitics.items():
        print(f"{k[:25]:>30}: {v}")
    print(f"{'*' * 30}")
