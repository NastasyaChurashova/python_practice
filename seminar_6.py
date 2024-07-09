'''
Задача №39. 
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива
Ввод:  
7 
3 1 3 4 2 4 12
6
4 15 43 1 15 1 (каждое число вводится с новой строки)
'''
# import random
# N = int(input("Введите количество элементов в первом массиве: "))
# lst_1 = [random.randint(1, 100) for _ in range(N)]
# print(lst_1)

# M = int(input("Введите количество элементов во втором массиве: "))
# lst_2 = [random.randint(1, 100) for _ in range(N)]
# print(lst_2)

# lst_1 = 3, 1, 3, 4, 2, 4, 12
# lst_2 = 4, 15, 43, 1, 15, 1

# def func(lst_1, lst_2):
#     new_lst = []
#     for el in lst_1:
#         if el not in lst_2:
#             new_lst.append(el)
#     return new_lst

# print(func(lst_1, lst_2))
# _______________________2 вариант_____________________________
# num_1 = [3, 1, 3, 4, 2, 4, 12]
# num_2 = [4, 15, 43, 1, 15, 1]
# num_3 = []
# num_5 = list(map(int, input('Введите числа через пробел...').split()))


# for el in num_1:
#     if el not in num_2:
#         num_3.append(el)
# print('Решение через традиционный итератор с функцией append')
# print(num_3)

# num_4 = [elem for elem in num_1 if elem not in num_2]
# print('\nРешение с применением List comprehension')
# print(num_4)

# res = filter(lambda elem: elem not in num_2, num_1)
# print('\nРешение через использование функций filter и lambda')
# print(', '.join(str(elem) for elem in res))
# ________________________3________________

# num_1 = [3, 1, 3, 4, 2, 4, 12]
# num_2 = [4, 15, 43, 1, 15, 1]
# num_3 = []
# num_5 = list(map(int, input('Введите числа через пробел...').split()))


# for el in num_1:
#     if el not in num_2:
#         num_3.append(el)
# print('Решение через традиционный итератор с функцией append')
# print(num_3)


# def func(num1, num2, num3=[]):
#     if len(num1) == 0:
#         return num3
#     if num1[0] not in num2:
#         num3.append(num1[0])
#     return func(num1[1:], num2, num3)


# print(func(num_1, num_2, num_3))

# num_4 = [elem for elem in num_1 if elem not in num_2]
# print('\nРешение с применением List comprehension')
# print(num_4)
#
# res = filter(lambda elem: elem not in num_2, num_1)
# print('\nРешение через использование функций filter и lambda')
# print(', '.join(str(elem) for elem in res))



'''
Задача №41. Решение в группах
Дан массив, состоящий из целых чисел. Напишите
программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при
этом, оба соседних элемента меньше данного. Сначала
вводится число N — количество элементов в массиве
Далее записаны N чисел — элементы массива. Массив
состоит из целых чисел.

Ввод: 
5 
1 2 3 4 5 
Вывод: 
0

Ввод:
5
1 5 1 5 1

Вывод:
2
(каждое число вводится с новой строки)

'''
# lst_numbers = []

# # Количество элементов, которое нужно ввести
# lst_len = 5

# # Ввод элементов построчно
# for _ in range(lst_len):
#     element = int(input("Введите элемент: "))
#     lst_numbers.append(element)

# # Вывод полученного списка
# print(lst_numbers)

# def func(lst_numbers):
#     count = 0
#     for i in range(1, len(lst_numbers) - 1):
#         if lst_numbers[i - 1] < lst_numbers[i] and lst_numbers[i + 1] < lst_numbers[i]:
#             count += 1
#     return count

# print(func(lst_numbers))
# _______________________________2 версия________________


'''
Задача №43. Решение в группах
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод: 1 2 3 2 3 
Вывод:
2
'''
# lst_numbers = []

# # Количество элементов, которое нужно ввести
# lst_len = 5

# for _ in range(lst_len):
#     element = int(input("Введите элемент: "))
#     lst_numbers.append(element)

# # Вывод полученного списка
# print(lst_numbers)

# lst_numbers = [1, 2, 3, 6, 3, 1, 2, 3, 2, 3, 3]
# def func(lst_numbers):
#     counts = {}
#     for num in lst_numbers:
#         if num in counts:
#             counts[num] += 1
#         else:counts[num] = 1

#     pairs = 0
#     for count in counts.values():
#         pairs += count // 2
#     return pairs

 
# print(func(lst_numbers))
# ______________________________2_version_____________

# nums = [1, 2, 3, 2, 3, 3, 3, 3]

# nums_set = set(nums)
# res = []

# for el in nums_set:
#     res.append(nums.count(el) // 2)
# print (sum(res))


'''
Задача №45. Решение в группах
Два различных натуральных числа n и m называются
дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и
наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных
чисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, не
превосходящее 105
. Программа должна вывести все
пары дружественных чисел, каждое из которых не
превосходит k. Пары необходимо выводить по одной в
строке, разделяя пробелами. Каждая пара должна быть
выведена только один раз (перестановка чисел новую
пару не дает).

Ввод:300  Вывод:  220 284
'''

# def sum_of_divisors(n):
#     return sum(i for i in range(1, n) if n % i == 0)

# def find_amicable_numbers(k):
#     found_pairs = set()
#     for n in range(1, k):
#         m = sum_of_divisors(n)
#         if m != n and sum_of_divisors(m) == n and m < k:
#             pair = tuple(sorted((n, m)))
#             if pair not in found_pairs:
#                 found_pairs.add(pair)
#                 print(f"{pair[0]} и {pair[1]} - дружественные числа")

# print(find_amicable_numbers(300))

# _______________via recursion__________________

#  from sys import setrecursionlimit


# k = int(input('k = '))
# setrecursionlimit(10**5)


# def pairs(array):
#     if len(array) == 0:
#         return
#     pairless = array.pop(0)
#     for i in array:
#         if i[0] == pairless[1] and i[1] == pairless[0]:
#             print(f'{pairless[0]} {i[0]}')
#     return pairs(array)


# def denominators(n, s=1, all_numbers_denominators=None):
#     if all_numbers_denominators is None:
#         all_numbers_denominators = []
#     if s > n:
#         return all_numbers_denominators
#     denominator_sum = 0
#     for i in range(1, s // 2 + 1):
#         if s % i == 0:
#             denominator_sum += i
#     all_numbers_denominators.append((s, denominator_sum,))
#     return denominators(k, s+1, all_numbers_denominators)


# pairs(denominators(k))

# **********************тема генераторов***************

def func1(n):
    res = [el for el in range(n)]
    return res

print(func1(5))


def func2(n):
    for el in range(n):
        yield el

for el in func2(5):
    print(el, end = ' ')

print((el for el in range(5)))
print({el: el for el in range(5)})