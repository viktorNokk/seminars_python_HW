# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

num_day = int(input('input days week: '))
if 1 <= num_day <= 5:
    print('not weekend')
elif 6 <= num_day <= 7:
    print('weekend')
else:
    print('wrong day')

# 2 Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            print(not (x or y or z) == (not x and not y and not z))


# 3 Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

x = int(input('input X: '))
y = int(input('input Y: '))

if x > 0 and y > 0:
    print('1th')
elif  x < 0 and y > 0:
    print('2th')
elif x < 0 and y < 0:
    print('3th')
elif x > 0 and y < 0:
    print('4th')
else:
    print('wrong - null')

# 4 Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

q_number = int(input('input quarter number: '))

if q_number == 1:
    print('1th quarter: x > 0 and y > 0')
elif q_number == 2:
    print('2th quarter: x < 0 and y > 0')
elif q_number == 3:
    print('3th quarter: x < 0 and y < 0')
elif q_number == 4:
    print('4th quarter: x > 0 and y < 0')
else:
    print('wrong quarter')

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

import math
x1, y1 = map(int, input('coordinates point A: ').split(','))
x2, y2 = map(int, input('coordinates point B: ').split(','))

s = round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)
print(s)

