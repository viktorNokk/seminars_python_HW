# 1. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# Способ 1
from decimal import *
n = Decimal(input('Input float number: '))
d = Decimal(input('Input precision: '))
result = n.quantize(d)

print(f'Number with precision is: {result}')

# Способ 2
n = float(input())
d = float(input())
if d == 1:
    print(int(n))
else:
    d = str(d)
    d = d.split('.')
    d = len(d[1])
    print(round(n, d))

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input('Input natural number: '))

factors = []
factors.append(1)
n = number

while n % 2 == 0:
    factors.append(2)
    n //= 2

for i in range(3, n // 2 + 1, 2):
    while n % i == 0:
        factors.append(i)
        n = n // i

if n!= 1:
    factors.append(n)

print(f'Number {number} can be factored {factors}')

# 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

# Вариант 1
n = int(input('Input numbers of elements: '))
original_list = []
for i in range(0, n):
    original_list.append(int(input('Input element: ')))
print(original_list, sep=', ')

set_original_list = set(original_list)
print(set_original_list)

# Вариант 2
a = [2 ,5, 8, 8, 3, 0, 3, 2]
b = []
for i in a:
    count = 0
    for j in a:
        if i == j:
            count += 1
        if count == 2:
            break
    if count == 1:
        print(i)

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
some_dict = {0: '^0', 1: '^1', 2: '^2', 3: '^3', 4: '^4', 5: '^5', 6: '^6', 7: '^7', 8: '^8', 9: '^9'}
k = int(input('Введите натуральную степень k: '))
koef = [random.randint(0, 100) for _ in range(k + 1)]
print(koef)
with open('koef.txt', 'w', encoding='utf-8') as m:
    for i in range(len(koef)):
        if k - i != 1 and k - i != 0:
            m.write(f'{koef[i]}x{some_dict[k - i]} + ')
        elif k - i == 1:
            m.write(f'{koef[i]}x + ')
        elif k - i == 0:
            m.write(f'{koef[i]} = 0')
