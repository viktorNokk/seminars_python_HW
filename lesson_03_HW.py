# 1. Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# Вариант со статическим списком
list1 = [2, 3, 5, 9, 3]
sum_odd_position = 0
for i in range(1, len(list1), 2):
    sum_odd_position = sum_odd_position + list1[i]
print(list1)
print(f'sum of odd positions is: {sum_odd_position}')
print()

# Вариант со случайным списком
from random import *
n = int(input('input numbers position in list: '))
some_list = []
for _ in range(n):
    some_list.append(randint(0,n))
print(some_list)

sum_odd_position = 0
for i in range(1, len(some_list), 2):
    sum_odd_position = sum_odd_position + some_list[i]
print(f'sum of odd positions is: {sum_odd_position}')

# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
# Вариант 1
from random import *
n = int(input('input numbers position in list: '))
some_list = []
for _ in range(n):
    some_list.append(randint(0,n))
print(some_list)

new_list = []
el = 0
for i in range(len(some_list) // 2):
    new_list.append(some_list[el] * some_list[len(some_list) - 1 - el])
    el+=1
if len(some_list) % 2 == 1:
    new_list.append(some_list[el] ** 2)
print(new_list)

# Вариант 2
count = int(input('Введите кол-во элементов: '))
some_list = []
for _ in range(count):
    number = int(input())
    some_list.append(number)
new_list = []
for idx in range((count - 1) // 2 + 1):
    number1 = some_list[idx]
    number2 = some_list[count - idx - 1]
    new_list.append(number1 * number2)
print(new_list)

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# Вариант 1
from random import *
n = int(input('input numbers position in list: '))
some_list = []
for _ in range(n):
    some_list.append(uniform(1.0, n))
print(some_list)

mini = round(some_list[0] - round(some_list[0]), 2)
maxi = round(some_list[0] - round(some_list[0]), 2)
for i in some_list:
    if mini > round(i - round(i), 2):
        mini = round(i - round(i), 2)
    if maxi < round(i - round(i), 2):
        maxi = round(i - round(i), 2)
result = maxi - mini
print(f'result max - min is: {result}')

# Вариант 2
count = int(input('input elements: '))
some_list = []
for _ in range(count):
    number = float(input())
    some_list.append(number)
minn = 1
maxx = 0
for el in some_list:
    if '.' in str(el):
        dr = str(el).split('.')[1]
        if float('0.' + dr) > maxx:
            maxx = float('0.' + dr)
        elif float('0.' + dr) < minn:
            minn = float('0.' + dr)
print(maxx - minn)

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное

n = int(input())
res = ''
while n > 0:
    res = str(n % 2) + res
    n = int(n / 2)
print(res)

# Через функцию
def change_digit(n):
    res = ''
    while n > 0:
        res = str(n % 2) + res
        n = int(n / 2)
    return res

n = int(input('input digital: '))
number = change_digit(n)
print(f'digit {n} convert to {number}')

# Вариант через bin
a = int(input())
print(bin(a)[2:]) # срез 1х 2х символов

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 

k = int(input())
some_list = [0] * (k * 2 + 1)
some_list[k + 1] = 1
for idx in range(k + 2, k * 2 + 1):
    some_list[idx] = some_list[idx - 1] + some_list[idx - 2]
for idx in range(k, -1, -1):
    some_list[idx] = some_list[idx + 2] - some_list[idx + 1]
print(some_list)
