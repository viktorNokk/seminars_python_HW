# 1. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from decimal import *
n = Decimal(input('Input float number: '))
d = Decimal(input('Input precision: '))
result = n.quantize(d)

print(f'Number with precision is: {result}')

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

n = int(input('Input numbers of elements: '))
original_list = []
for i in range(0, n):
    original_list.append(int(input('Input element: ')))
print(original_list, sep=', ')

set_original_list = set(original_list)
print(set_original_list)