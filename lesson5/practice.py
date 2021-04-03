# Чтение файла (Фаил надо закрывать )
# wood = open(r"F:\2020\geekbrains\lesson5\text_303.txt", "r", encoding="utf-8")
# content = wood.read()   # Читает весь фаил (Строка)
# content1 = wood.readline()   # Читает по одной строке из файла (Строка)
# content2 = wood.readlines()   # Возвращает список
# wood.close()


# Запись в фаил

# Режимы записи:
# w - Создаст или зачистит фаил (Нельзя читать фаил)
# wood = open(r"F:\2020\geekbrains\lesson5\text_303.txt", "w", encoding="utf-8")
#
# wood.close()


# try:
#     with open(r"F:\2020\geekbrains\lesson5\text_303.txt", "r", encoding="utf-8") as wood:
#         wood.writelines(f"56 76 78\n{[1, 2, 3, 4]}\n{23, 56, 67}\n")
# except IOError:
#     print('Error!')




# with open(r"F:\2020\geekbrains\lesson5\text_303.txt", "a+", encoding="utf-8") as wood:
#     wood.writelines(f"56 76 78\n{[1, 2, 3, 4]}\n{23, 56, 67}\n")
#     wood.seek(0)
    # print(wood.read())

# print(wood.name)
# print(wood.mode)
# print(wood.closed)


# with open(r"F:\2020\geekbrains\lesson5\text_303.txt", "a", encoding="utf-8") as wood:
#     # wood.seek(8)
#     # print(wood.tell())
#     print("Python", file=wood)


import json


# data = {
#     "income": {
#         "salary": 50000,
#         "bonus": 20000
#     }
# }
#
#
# with open("my_file.json", "w", encoding="utf-8") as write_f:
#     json.dump(data, write_f)
#
#
# js_str = json.dumps(data)
# print(js_str)


with open("my_file.json", encoding="utf-8") as fead_f:
    data = json.load(fead_f)

data2 = {'income': {'salary': 50000, 'bonus': 20000}}

# print(data)
print(type(data2))

















