# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1 = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разность прогрессии: "))
n = int(input("Введите количество элементов прогрессии: "))
progression = []
for i in range(1, n + 1):
    an = a1 + (i - 1) * d
    progression.append(an)
print(progression)

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума). Список можно задавать рандомно

import random
min_value = int(input("Введите минимальное значение: "))
max_value = int(input("Введите максимальное значение: "))
my_massive = [random.randint(0, 100) for _ in range(10)]
filtered = [index for index, value in enumerate(my_massive) if min_value <= value <= max_value]
print(filtered)