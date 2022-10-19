# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

# Вариант 1
num = input('input value: ')
sum_num = 0
for i in str(num):
    if i != '.': # if i.isdigit():
        sum_num = sum_num + int(i)

print(f'sum of values is: {sum_num}')

# Вариант 2 (для целых чисел)
number = float(input)
summ = 0
while number != 0:
    summ += number % 10
    number //= 10
print(summ)


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

# Задание списка от - N до N
# n = int(input('Input N: '))
# some_list = []
# for i in range(-N, N + 1):
#     some_list.append(i)
# print(some_list)

# Задание рандомного списка
from random import *
n = int(input())
some_list = []
for _ in range(n):
    some_list.append(randint(-n, n))
print(some_list)

with open ('file.txt', 'w', encoding='utf-8') as f:
    for _ in range(randint(1, n)):
        f.write(str(randint(0, n - 1)) + '\n')
fact = 1 # переменная для произведения
with open ('file.txt', 'r', encoding='utf-8') as f:
    f = f.read().splitlines() # генерация из всех строк один список
    for number in f:
        fact *= some_list[int(number)]
print(fact)

# 5. Реализуйте алгоритм перемешивания списка

# Вариант shuffle
import random

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(list1)

print(list1)

# Вариант алгоритмом
import time
random_number = str(time.time()).split('.')[1]
some_list = [1, 4, 9, 10]
for _ in range(int(str(time.time()).split('.')[1]) % (10 - 5 + 1) + 5):
    i1 = int(str(time.time()).split('.')[1]) % (4 - 0) + 0
    time.sleep(0.00001)
    i2 = int(str(time.time()).split('.')[1]) % (4 - 0) + 0
    some_list[i1], some_list[i2] = some_list[i2], some_list[i1]
print(some_list)

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

