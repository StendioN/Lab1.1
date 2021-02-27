# Частина 1
import random

# Дано рядок у форматі "Student1 - Group1; Student2 - Group2; ..."

studentsStr = "Дмитренко Олександр - ІП-84; Матвійчук Андрій - ІВ-83; Лесик Сергій - ІО-82; Ткаченко Ярослав - ІВ-83; " \
              "Аверкова Анастасія - ІО-83; Соловйов Даніїл - ІО-83; Рахуба Вероніка - ІО-81; Кочерук Давид - ІВ-83; " \
              "Лихацька Юлія - ІВ-82; Головенець Руслан - ІВ-83; Ющенко Андрій - ІО-82; Мінченко Володимир - ІП-83; " \
              "Мартинюк Назар - ІО-82; Базова Лідія - ІВ-81; Снігурець Олег - ІВ-81; Роман Олександр - ІО-82; " \
              "Дудка Максим - ІО-81; Кулініч Віталій - ІВ-81; Жуков Михайло - ІП-83; Грабко Михайло - ІВ-81; " \
              "Иванов Володимир - ІО-81; Востриков Нікіта - ІО-82; Бондаренко Максим - ІВ-83; " \
              "Скрипченко Володимир - ІВ-82; Кобук Назар - ІО-81; Дровнін Павло - ІВ-83; Тарасенко Юлія - ІО-82; " \
              "Дрозд Світлана - ІВ-81; Фещенко Кирил - ІО-82; Крамар Віктор - ІО-83; Иванов Дмитро - ІВ-82"

# Завдання 1
# Заповніть словник, де:
# - ключ – назва групи
# - значення – відсортований масив студентів, які відносяться до відповідної групи

studentsGroups = {}

# Ваш код починається тут
pairs = []
IO81, IO82, IO83, IV81, IV82, IV83, IP83, IP84 = [], [], [], [], [], [], [], []
studentgroup = studentsStr.split("; ")
for i in studentgroup:
    i = i.split(" - ")
    pairs.append(i)
for i in range(0, 31):
    if "ІО-81" in pairs[i]:
        IO81.append(pairs[i][0])
        IO81.sort()
for i in range(0, 31):
    if "ІО-82" in pairs[i]:
        IO82.append(pairs[i][0])
        IO82.sort()
for i in range(0, 31):
    if "ІО-83" in pairs[i]:
        IO83.append(pairs[i][0])
        IO83.sort()
for i in range(0, 31):
    if "ІВ-81" in pairs[i]:
        IV81.append(pairs[i][0])
        IV81.sort()
for i in range(0, 31):
    if "ІВ-82" in pairs[i]:
        IV82.append(pairs[i][0])
        IV82.sort()
for i in range(0, 31):
    if "ІВ-83" in pairs[i]:
        IV83.append(pairs[i][0])
        IV83.sort()
for i in range(0, 31):
    if "ІП-83" in pairs[i]:
        IP83.append(pairs[i][0])
        IP83.sort()
for i in range(0, 31):
    if "ІП-84" in pairs[i]:
        IP84.append(pairs[i][0])
        IP84.sort()
studentsGroups.setdefault('IO-81', IO81)
studentsGroups.setdefault('IO-82', IO82)
studentsGroups.setdefault('IO-83', IO83)
studentsGroups.setdefault('IВ-81', IV81)
studentsGroups.setdefault('IВ-82', IV82)
studentsGroups.setdefault('IВ-83', IV83)
studentsGroups.setdefault('IП-83', IP83)
studentsGroups.setdefault('IП-84', IP84)
# Ваш код закінчується тут

print("Завдання 1")
print(studentsGroups)
print()

# Дано масив з максимально можливими оцінками

points = [12, 12, 12, 12, 12, 12, 12, 16]

# Завдання 2
# Заповніть словник, де:
# - ключ – назва групи
# - значення – словник, де:
#   - ключ – студент, який відносяться до відповідної групи
#  - значення – масив з оцінками студента (заповніть масив випадковими значеннями)

studentPoints = {}


# Ваш код починається тут
def random_numbers():
    random_list = [random.randint(0, 12) for j in range(7)]
    random_list.append(random.randint(0, 16))
    return random_list


dict1, dict2, dict3, dict4, dict5, dict6, dict7, dict8 = {}, {}, {}, {}, {}, {}, {}, {}
for i in IO81:
    dict1.setdefault(i, random_numbers())
for i in IO82:
    dict2.setdefault(i, random_numbers())
for i in IO83:
    dict3.setdefault(i, random_numbers())
for i in IV81:
    dict4.setdefault(i, random_numbers())
for i in IV82:
    dict5.setdefault(i, random_numbers())
for i in IV83:
    dict6.setdefault(i, random_numbers())
for i in IP83:
    dict7.setdefault(i, random_numbers())
for i in IP84:
    dict8.setdefault(i, random_numbers())
studentPoints.update({'IO-81': dict1})
studentPoints.update({'IO-82': dict2})
studentPoints.update({'IO-83': dict3})
studentPoints.update({'IВ-81': dict4})
studentPoints.update({'IВ-82': dict5})
studentPoints.update({'IВ-83': dict6})
studentPoints.update({'IП-83': dict7})
studentPoints.update({'IП-84': dict8})
# Ваш код закінчується тут

print("Завдання 2")
print(studentPoints)
print()

# # Завдання 3
# # Заповніть словник, де:
# # - ключ – назва групи
# # - значення – словник, де:
# #   - ключ – студент, який відносяться до відповідної групи
# #   - значення – сума оцінок студента

sumPoints = {}

# # Ваш код починається тут
sumPoints = studentPoints.copy()
for keys, values in sumPoints.items():
    for key, value in values.items():
        b = sum(value)
        values.update({key: b})
    sumPoints.update({keys: values})
# # Ваш код закінчується тут

print("Завдання 3")
print(sumPoints)
print()

# # Завдання 4
# # Заповніть словник, де:
# # - ключ – назва групи
# # - значення – середня оцінка всіх студентів групи

groupAvg = {}

# # Ваш код починається тут
c = []
d = []
e = 0
groupAvg = studentPoints.copy()
for keys, values in groupAvg.items():
    for key, value in values.items():
        c.append(value)
        e = sum(c) / len(c)
    d.append(e)
    e = 0
    c.clear()
groups = groupAvg.keys()
groupAvg = dict(zip(groups, d))

# # Ваш код закінчується тут

print("Завдання 4")
print(groupAvg)
print()

# # Завдання 5
# # Заповніть словник, де:
# # - ключ – назва групи
# # - значення – масив студентів, які мають >= 60 балів

passedPerGroup = {}

# # Ваш код починається тут
dictionary = sumPoints.copy()
for keys, values in dictionary.items():
    student_list = []
    for key, value in values.items():
        if value >= 60:
            student_list.append(key)
    passedPerGroup.update({keys: student_list})
# # Ваш код закінчується тут

print("Завдання 5")
print(passedPerGroup)


