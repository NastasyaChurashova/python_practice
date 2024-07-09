'''
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).
На вход подается список с элементами list_1 и границы диапазона в виде чисел min_number, max_number.
на входе:
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10

На выходе:
1
2
3
6
7
9
10
11
13
14
16
19

'''
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_number = 0
max_number = 10

# for i in range(0, len(list_1)):
#     if min_number <= list_1[i] <= max_number:
#         print(i)

# indices = [index for index, value in enumerate(list_1) if min_number <= value <= max_number]

# for index in indices:
#     print(index)

'''
Заполните массив элементами арифметической прогрессии. Её первый элемент a1 , разность d и количество элементов n будет задано автоматически. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
на входе:
a1 = 2
d = 3
n = 4

на выходе: 
2
5
8
11
'''

a1 = 2
d = 3
n = 4

def func(a1, d, n):
    progression = (a1 + (i-1) * d for i in range(1, n+1))
    for elem in progression:
        print(elem)

func(a1, d, n)