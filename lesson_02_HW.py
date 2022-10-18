# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

num = input('input value: ')

sum_num = 0
for i in str(num):
    if i != '.':
        sum_num = sum_num + int(i)

print(f'sum of values is: {sum_num}')

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = int(input('Input N: '))
result = 1
a = []

for i in range(1, N + 1):
    result = result * i
    a.append(result)

print(*a, sep=', ')

# 3. Задайте список из n чисел последовательности (1+ 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# сумма 9,06

n = int(input('input n: '))
sum_n = 0

for i in range(n):
    sum_n = round((sum_n + (1 + 1 / (i+1)) ** (i+1)), 2)
print(f'sum is: {sum_n}')  

# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число (в разработке)

N = int(input('Input N: '))
list1 = []
for i in range(-N, N + 1):
    list1.append(i)
print(list1)

# with open('SeminarsPythonHW/file.txt', 'r', encoding='utf-8'):

# 5. Реализуйте алгоритм перемешивания списка

import random

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(list1)

print(list1)

# 6. ДОП. задача на алгоритмы с реальных собеседований
# Даны два массива:
# [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение
# [1, 2, 2, 3]
# (порядок не важен)

list1 = [1, 2, 3, 2, 0]
list2 = [5, 1, 2, 7, 3, 2]

set1 = set(list1)
set2 = set(list2)

dif = set1.intersection(set2)

print(dif)

